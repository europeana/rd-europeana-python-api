import os
import urllib
import requests

from schema import Schema, And, Use, Optional

from .edm import *
from .utils import *
from .responses import *




class EuropeanaAPI:

    """
    Python wrapper for Europeana's API

    Get your API key here: https://pro.europeana.eu/pages/get-api

    Usage:

        from europeana.api import EuropeanaAPI
        eu = EuropeanaAPI('your_API_key')
        r = eu.search('Amsterdam', theme = 'nature')
        print('total number of results: {}'.format(r['totalResults']))

    Attributes:

        eu.wskey
        eu.accepted_arguments
        eu.themes

    Methods:
        Search: help(eu.search)
        Record: help(eu.record)

    """

    def __init__(self,wskey):
        self.wskey = wskey
        self.search_API_url = 'https://www.europeana.eu/api/v2/search.json?'
        self.accepted_arguments = ['n','rows', 'start', 'media', 'what', 'where', 'who', 'range','lat','lon','reusability','thumbnail','landingpage', 'theme','sort']
        self.refined_search_arguments = ['what','where','who','lat','lon','range']
        self.themes = ['archaeology','art','fashion','industrial','manuscript','map','migration','music','nature','newspaper','photography','sport','ww1']


        self.validation_dict = {
            # basic parameters
            'rows':validate_rows,
            'start':validate_start,
            'media':validate_media,
            'logic':validate_logic,
            'reusability':validate_reusability,
            'thumbnail':validate_thumbnail,
            'landingpage':validate_landingpage,
            'sort': validate_sort,

            # refined search parameters
            'what':format_what,
            'where':format_where,
            'who':format_who,
            'lat':format_lat,
            'lon':format_lon,
            'range':format_range,
        }



    def record(self, record_id):
        """
        Wrapper for Europeana's Record API;

        Input: 
            record_id: string
                id of the cultural heritage object

        Response:
            raw Europeana API response

        """
        try:
            url = f'https://www.europeana.eu/api/v2/record{record_id}.json?'
            return requests.get(url, params = {'wskey':self.wskey}).json()
        except:
            print(f'WARNING: Error in Europeana record API, the ID "{record_id}" might not exist')
            pass

 


    def _search_multipage(self, query, **kwargs):

        args_page_search = {k:v for k,v in kwargs.items() if k not in ['n']}
        # number of requested results
        req_num = kwargs['n']
        # number of pages to search and number of items in the last page
        n_pages, rest = req_num//100+1, req_num%100
        start_list = [i for i in range(1,n_pages)]+[n_pages]
        rows_list = [100 for i in range(1,n_pages)]+[rest]
        #initialize the search results
        #results = {'items':[]}
        item_list = []
        for start, rows in zip(start_list, rows_list):
            # update page search arguments
            args_page_search.update({'start':start,'rows':rows})
            #print(args_page_search)
            # search page
            response = self._search_page(query, **args_page_search)
            #print(response)
            if response and response['success']:
                # include page results 
                item_list += response['items']
                # include number of total results
                #results.update({'totalResults':response['totalResults']})
            else:
                print('EuropeanaAPI: error requesting page {}, skipping results'.format(start))
        
        response.update({'items':item_list})
        return response

    def _search_page(self,query,**kwargs):
        params = kwargs.copy()
        params.update({'query':query})
        try: 
            response = requests.get(self.search_API_url, params = params).json()
            return response
        except:
            print('something went wrong')
            

    def search(self, query, **kwargs):
        """
        Interface for Europeana's search API

        Parameters
        ----------
        query : string
          Needless description

        n :  0 <= int <= 10000
          Number of objects to request. Not compatible with arguments "rows" and "start"

        rows :  0 <= int <= 100  default = 12
          Number of objects to request if single page request. Not compatible with argument "n"

        start :  1 <= int <= 100  default = 1
          Page number if single page request. Not compatible with argument "n"
        
        where : string
          Location of the cultural heritage object

        who : string
          Author of the work

        lat : [float,float]
          Latitude of the work

        lon : [float,float]
          Longitude of the work

        range: [string,string]
          ***Description needed***

        media :  bool  default = True
          Whether the results should have media

        reusability :  str in ['open','restricted','permission']
          Rights for using the data

        thumbnail :  bool  default = True
          Whether the results should have thumbnails

        landingpage : bool default = False
          ***Description needed***

        theme :  str in ['archaeology','art','fashion','industrial',
          'manuscript','map','migration','music','nature',
          'newspaper','photography','sport','ww1']


        sort : dict {'term':value,'order':value}
            'term' value : str in ['score', 'timestamp_created', 'timestamp_update', 'europeana_id', 'COMPLETENESS', 'is_fulltext', 'has_thumbnails', 'has_media']
            'order' value : str in ['asc','desc']

          

        """

        # default arguments
        params = {'wskey':self.wskey, 'logic':'AND'}
        validation_dict = self.validation_dict
        # refined search list
        qf_list = []

        # check for unexpected arguments
        for key in kwargs.keys():
            if key not in self.accepted_arguments:
                raise ValueError(f'EuropeanaAPI: "{key}" argument not accepted, only those in {self.accepted_arguments}') 
            
            #basic parameters
            if key == 'media':
                params.update({key:validation_dict[key](kwargs[key])})
            if key == 'logic':
                params.update({key:validation_dict[key](kwargs[key])})
            if key == 'reusability':
                params.update({key:validation_dict[key](kwargs[key])})
            if key == 'thumbnail':
                params.update({key:validation_dict[key](kwargs[key])})
            if key == 'theme':
                params.update({key:self.validate_theme(kwargs[key])})
            if key == 'sort':
                params.update({key:validation_dict[key](kwargs[key])})
            if key == 'landingpage':
                params.update({key:validation_dict[key](kwargs[key])})

            # refined search parameters
            if key == 'where':
                qf_list.append(validation_dict[key](kwargs[key]))
            if key == 'who':
                qf_list.append(validation_dict[key](kwargs[key]))
            if key == 'lat':
                qf_list.append(validation_dict[key](kwargs[key]))
            if key == 'lon':
                qf_list.append(validation_dict[key](kwargs[key]))

        # the range argument must be at the end of the query
        if 'range' in kwargs:
            qf_list.append(validation_dict[key](kwargs[key]))

        qf_str = ' {} '.format(params['logic']).join(qf_list)
        params.update({'qf':qf_str})

    
        # multipage search
        if 'n' in kwargs:

            # force either multipage or single page search
            if 'rows' in kwargs or 'start' in kwargs:
                raise ValueError('EuropeanaAPI: "n" is incompatible with "rows" or "start"')
            
            # validate n
            params.update({'n':self.validate_n(query,params,**kwargs)})
            
            response = self._search_multipage(query, **params)
            return SearchResponse(response,query,**params)
    
        # single page search
        else:

            # validate rows and start
            params.update({'rows':12,'start':1})
            if 'rows' in kwargs:
                key = 'rows'
                params.update({key:validation_dict[key](kwargs[key])})
            if 'start' in kwargs:
                key = 'start'
                params.update({key:validation_dict[key](kwargs[key])})

            response = self._search_page(query, **params)
            #print(response.keys())
            #print(response['success'])
            return SearchResponse(response,query,**params)


    def test_request(self, query, **kwargs):
        params = kwargs.copy()
        if 'rows' not in params.keys():
            params.update({'rows':1})
        
        totalResults = 0
        response = self._search_page(query, **params)
        if response['success']:
            totalResults = response['totalResults']

        else:
            print('Something went wrong with the test_request')
        return totalResults


    def validate_n(self,query,params,**kwargs):
        n = kwargs['n']
        try:
            n = Schema(And(Use(int), lambda x: 1 <= x <= 10000)).validate(n) 
            totalResults = self.test_request(query,**params)
            if n > totalResults:
                n = totalResults
                print('WARNING: EuropeanaAPI: "n" greater than the number of results. "n" set to {}'.format(totalResults))
            return n
        except:
            raise ValueError('EuropeanaAPI: n must be a positive integer smaller than 10000')

    
    def validate_theme(self,theme):
        try:
            return Schema(And(Use(str), lambda n: n in self.themes)).validate(theme)
        except:
            raise ValueError(f'EuropeanaAPI: "theme" must be in {self.themes}')




    

