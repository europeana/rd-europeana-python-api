import requests
import pandas as pd

from pyeuropeana.utils.edm_utils import europeana_id2uri

def cursor_search(params):
    CHO_list = []
    response = {'nextCursor':params['cursor']}
    while 'nextCursor' in response:
      if len(CHO_list)>params['rows']:
        break
      params.update({'cursor':response['nextCursor']})
      response = requests.get('https://api.europeana.eu/record/v2/search.json', params = params).json()
      CHO_list += response['items']
    CHO_list = CHO_list[:params['rows']]
    response['items'] = CHO_list
    return response

class Search:
  def __init__(self,wskey):
    self.wskey = wskey
    response = requests.get('https://api.europeana.eu/record/v2/search.json', params = {'wskey':wskey,'query':'*'}).json()
    if not response['success']:
      raise ValueError(response['error'])
      
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
