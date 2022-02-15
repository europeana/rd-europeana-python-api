import requests
import pandas as pd

import warnings

# to do: enforce media, thumnail and landing page as boolean
# to do: enforce rows to be a number
# to do: enforce other variables to be strings
# to do: test for facets
# to do: throw a warning when reusability is not in ['open','permission','restricted']
# to do: test utils

def SearchWrapper(**kwargs):
  """
  Wrapper for the Search API

  Parameters
  ----------
  wskey : str
      The api key. Get an api key here (?)
  query : str
      The query (default is '*') https://pro.europeana.eu/page/search#syntax
  qf : int, optional
      Query refinament
  reusability : str, optional
    Reusability: 
  media : int, optional
    The number of legs the animal (default is 4)
  thumbnail : int, optional
    The number of legs the animal (default is 4)
  landingpage : int, optional
    The number of legs the animal (default is 4)
  colourpalette : int, optional
    The number of legs the animal (default is 4)
  theme : int, optional
    The number of legs the animal (default is 4)
  sort : int, optional
    The number of legs the animal (default is 4)
  profile : int, optional
    The number of legs the animal (default is 4)
  rows : int, optional
    The number of legs the animal (default is 4)
  cursor : int, optional
    The number of legs the animal (default is 4)
  callback : int, optional
    The number of legs the animal (default is 4)
  facet : int, optional
    The number of legs the animal (default is 4)
  
  """
  params = {
      'wskey':kwargs.get('wskey'),
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

  if not kwargs:
    raise ValueError('No arguments passed')

  # test key
  response = requests.get('https://api.europeana.eu/record/v2/search.json', params = {'wskey':params['wskey'],'query':'*'}).json()
  if not response['success']:
    raise ValueError(response['error'])

  # careful with this: are we expecting arguments other than the ones in params?
  wrong_args = [args for args in kwargs.keys() if args not in params]
  if wrong_args:
    raise ValueError(f"Invalid arguments detected: {wrong_args}")

  url = requests.get('https://api.europeana.eu/record/v2/search.json', params = params).url
  response =  cursor_search(params)
  response.update({'url':url,'params':params})
  return response  
 

def cursor_search(params):
  """
  Cursor search function
  """
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

class SearchAPI:
  """
  Wrapper for the Search API
  """
  def __init__(self,wskey):
    self.wskey = wskey
    response = requests.get('https://api.europeana.eu/record/v2/search.json', params = {'wskey':wskey,'query':'*'}).json()
    if not response['success']:
      raise ValueError(response['error'])
      
  def __call__(self,**kwargs):
    """
    Description of call
    """
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

    if not kwargs:
      raise ValueError('No arguments passed')

    # careful with this: are we expecting arguments other than the ones in params?
    wrong_args = [args for args in kwargs.keys() if args not in params]
    if wrong_args:
      raise ValueError(f"Invalid arguments detected: {wrong_args}")


    # to do: enforce media, thumnail and landing page as boolean
    # to do: enforce rows to be a number
    # to do: enforce other variables to be strings
    # to do: test for facets
    # to do: throw a warning when reusability is not in ['open','permission','restricted']
    # to do: test utils

    url = requests.get('https://api.europeana.eu/record/v2/search.json', params = params).url
    response =  cursor_search(params)
    response.update({'url':url,'params':params})
    return response  
