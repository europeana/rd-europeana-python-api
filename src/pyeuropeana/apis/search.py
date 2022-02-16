import requests

from ..utils.auth import get_api_key

def search(**kwargs):
  """
  Wrapper for the Search API

  >>> from pyeuropeana.apis import SearchWrapper
  >>> resp = SearchWrapper(
  >>>    query = 'Paris',
  >>>    qf = 'TYPE:IMAGE',
  >>>    rows = 150,
  >>>     )

  Parameters
  ----------
  query : str
      The search term(s). See Query Syntax [?] for information on forming complex queries and examples.
  qf : int, optional
      Query Refinement. This parameter can be defined more than once. See Query Syntax [?] page for more information.
  reusability : str, optional
    Filter by copyright status. Possible values are open, restricted or permission.
  media : bool, optional
    Filter by records where an URL to the full media file is present in the edm:isShownBy or edm:hasView metadata and is resolvable.
  thumbnail : bool, optional
    Filter by records where a thumbnail image has been generated for any of the WebResource media resources (thumbnail available in the edmPreview field).
  landingpage : bool, optional
    Filter by records where the link to the original object on the providers website (edm:isShownAt) is present and verified to be working.
  colourpalette : str, optional
    Filter by images where one of the colours (see colour palette) of an image matches the provided colour code. You can provide this parameter multiple times, the search will then do an 'AND' search on all the provided colours.
  theme : str, optional
    Restrict the query over one of the Europeana Thematic Collections. The possible values are: archaelogy, art, fashion, industrial, manuscript, map, migration, music, nature, newspaper, photography, sport, ww1.
  sort : str, optional
    Sorting records in ascending or descending order of search fields. The following fields are supported: score (relenvancy of the search result), timestamp_created, timestamp_update, europeana_id, COMPLETENESS, is_fulltext, has_thumbnails, and has_media. Sorting on more than one field is possible by supplying as comma separated values. It is also possible to randomly order items by using the keyword "random" instead of a field name. You can also request for a fixed random order by indicating a seed "random_SEED" which is useful when paginating along the same randomized order.
  profile : str, optional
    	A profile parameter which controls the format and richness of the response.
  rows : int, optional
    The number of records to return. Maximum is 100. Defaults to 12. See pagination.
  cursor : str, optional
    A cursor mark from where to start the search result set when using deep pagination. Set to * to start cursor-based pagination.
  callback : str, optional
   	Name of a client side callback function, see JSONP.
  facet : str, optional
    A name of an individual field or a comma separated list of fields
  
  """
  params = {
      'wskey':get_api_key(),
      'query':kwargs.get('query'), 
      'qf':kwargs.get('qf'),
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

# class SearchAPI:
#   """
#   Wrapper for the Search API
#   """
#   def __init__(self,wskey):
#     self.wskey = wskey
#     response = requests.get('https://api.europeana.eu/record/v2/search.json', params = {'wskey':wskey,'query':'*'}).json()
#     if not response['success']:
#       raise ValueError(response['error'])
      
#   def __call__(self,**kwargs):
#     """
#     Description of call
#     """
#     params = {
#         'wskey':self.wskey,
#         'query':kwargs.get('query','*'), 
#         'qf':kwargs.get('qf',''),
#         'reusability':kwargs.get('reusability'),
#         'media':kwargs.get('media'),
#         'thumbnail':kwargs.get('thumbnail'),
#         'landingpage':kwargs.get('landingpage'),
#         'colourpalette':kwargs.get('colourpalette'),
#         'theme':kwargs.get('theme'),
#         'sort':kwargs.get('sort','europeana_id'),
#         'profile':kwargs.get('profile'),
#         'rows':kwargs.get('rows',12),
#         'cursor':kwargs.get('cursor','*'),
#         'callback':kwargs.get('callback'),   
#         'facet':kwargs.get('facet'),
#     }

#     if not kwargs:
#       raise ValueError('No arguments passed')

#     # careful with this: are we expecting arguments other than the ones in params?
#     wrong_args = [args for args in kwargs.keys() if args not in params]
#     if wrong_args:
#       raise ValueError(f"Invalid arguments detected: {wrong_args}")


#     # to do: enforce media, thumnail and landing page as boolean
#     # to do: enforce rows to be a number
#     # to do: enforce other variables to be strings
#     # to do: test for facets
#     # to do: throw a warning when reusability is not in ['open','permission','restricted']
#     # to do: test utils

#     url = requests.get('https://api.europeana.eu/record/v2/search.json', params = params).url
#     response =  cursor_search(params)
#     response.update({'url':url,'params':params})
#     return response  
