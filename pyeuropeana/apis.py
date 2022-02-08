import requests
import pandas as pd

from .utils import europeana_id2uri

def get_value_lang(lang_dict):
    if 'en' in lang_dict.keys():
      value = lang_dict['en']
    else:
      _ , value = list(lang_dict.items())[0]
    return value

def process_CHO_record(response):
    obj = response['object']
    europeana_id = obj['about']

    try:
      image_url = obj['aggregations'][0]['edmIsShownBy']
    except:
      image_url = None

    # getting title
    proxy_list = obj['proxies']
    proxy_dict = {}
    for proxy in proxy_list:
      proxy_dict.update(proxy)

    title_lang = proxy_dict['dcTitle'] if 'dcTitle' in proxy_dict else None
    title = None
    if title_lang:
      title_lang = {k:v[0] for k,v in title_lang.items()}
      title = get_value_lang(title_lang)
      
    # getting provider
    provider_lang = obj['aggregations'][0]['edmProvider']
    provider_lang = {k:v[0] for k,v in provider_lang.items()}
    provider = get_value_lang(provider_lang)

    return {
        'raw_metadata': response,
        'europeana_id': europeana_id,
        'image_url': image_url,
        'uri': europeana_id2uri(europeana_id),
        'dataset_name': obj['edmDatasetName'][0],
        'country': obj['europeanaAggregation']['edmCountry']['def'][0],
        'language': obj['europeanaAggregation']['edmLanguage']['def'][0],
        'type': obj['type'],
        'title': title,
        'title_lang': title_lang,
        'rights': obj['aggregations'][0]['edmRights']['def'][0],
        'provider': provider,
        'provider_lang': provider_lang,
    }

def cursor_search(params):
    CHO_list = []
    response = {'nextCursor':'*'}
    #url = None
    while 'nextCursor' in response:
      if len(CHO_list)>params['rows']:
        break
      params.update({'cursor':response['nextCursor']})
      response = requests.get('https://api.europeana.eu/record/v2/search.json', params = params) 
      #if url is None:
      #  url = raw_response.url

      response = response.json()
      #totalResults = raw_response['totalResults']

      # to do: return if response is false
      CHO_list += response['items']

    CHO_list = CHO_list[:params['rows']]
    response['items'] = CHO_list
    return response


class Search:
  def __init__(self,wskey):
    self.wskey = wskey
  def __call__(self,**kwargs):
    params = {
        'wskey':self.wskey,
        'query':kwargs.get('query','*'), 
        'qf':kwargs.get('qf',''),
        'reusability':kwargs.get('reusability'),
        'media':kwargs.get('media'),
        'thumbnail':kwargs.get('thumbnail'),
        'landingpage':kwargs.get('landingpage'),
        'colourpalette':kwargs.get('colourpalette'),
        'theme':kwargs.get('theme'),
        'sort':kwargs.get('sort','europeana_id'),
        'profile':kwargs.get('profile'),
        'rows':kwargs.get('rows',12),
        'cursor':kwargs.get('cursor','*'),
        'callback':kwargs.get('callback'),   
        'facet':kwargs.get('facet'),
    }

    url = requests.get('https://api.europeana.eu/record/v2/search.json', params = params).url
    response =  cursor_search(params)
    response.update({'url':url,'params':params})
    return response

    # return SearchResponse(
    #     CHO_list = [process_CHO_search(item) for item in CHO_list], 
    #     params = params,
    #     url = url,
    #     totalResults = totalResults,
    #     raw_response = raw_response
    #     )
     

class Record:
  def __init__(self,wskey):
    self.wskey = wskey
  def __call__(self,id):
    params = {'wskey':self.wskey}
    response = requests.get(f'https://api.europeana.eu/record/v2/{id}.json',params=params).json()  
    return process_CHO_record(response)
    


