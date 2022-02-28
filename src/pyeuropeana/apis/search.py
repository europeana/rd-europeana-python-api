import requests

from ..utils.auth import get_api_key
from ..utils.edm_utils import cursor_search

def search(**kwargs):
  """
  Wrapper for the Search API [1]. Returns objects matching a query with several parameters

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.search(
  >>>    query = '*',s
  >>>    qf = 'TYPE:IMAGE',
  >>>    reusability = 'open AND permission',
  >>>    media = True,
  >>>    thumbnail = True,
  >>>    colourpalette = '#0000FF',
  >>>    theme = 'photography',
  >>>    sort = 'europeana_id',
  >>>    profile = 'rich',
  >>>    rows = 1000,
  >>>     )

  Args:
    query (:obj:`str`)
        The search term(s). See Query Syntax [?] for information on forming complex queries and examples.
    rows (:obj:`int`,optional)
      The number of records to return. Maximum is 100. Defaults to 12. See pagination.
    qf (:obj:`str`,optional)
        Query Refinement. This parameter can be defined more than once. See Query Syntax [?] page for more information.
    reusability (:obj:`str`,optional)
      Filter by copyright status. Possible values are open, restricted or permission.
    media (:obj:`bool`,optional)
      Filter by records where an URL to the full media file is present in the edm:isShownBy or edm:hasView metadata and is resolvable.
    thumbnail (:obj:`bool`,optional)
      Filter by records where a thumbnail image has been generated for any of the WebResource media resources (thumbnail available in the edmPreview field).
    landingpage (:obj:`bool`,optional)
      Filter by records where the link to the original object on the providers website (edm:isShownAt) is present and verified to be working.
    colourpalette (:obj:`str`,optional)
      Filter by images where one of the colours (see colour palette) of an image matches the provided colour code. You can provide this parameter multiple times, the search will then do an 'AND' search on all the provided colours.
    theme (:obj:`str`,optional)
      Restrict the query over one of the Europeana Thematic Collections. The possible values are: archaelogy, art, fashion, industrial, manuscript, map, migration, music, nature, newspaper, photography, sport, ww1.
    sort (:obj:`str`,optional)
      Sorting records in ascending or descending order of search fields. The following fields are supported: score (relenvancy of the search result), timestamp_created, timestamp_update, europeana_id, COMPLETENESS, is_fulltext, has_thumbnails, and has_media. Sorting on more than one field is possible by supplying as comma separated values. It is also possible to randomly order items by using the keyword "random" instead of a field name. You can also request for a fixed random order by indicating a seed "random_SEED" which is useful when paginating along the same randomized order.
    profile (:obj:`str`,optional)
      A profile parameter which controls the format and richness of the response.
    cursor (:obj:`str`,optional)
      A cursor mark from where to start the search result set when using deep pagination. Set to * to start cursor-based pagination.
    callback (:obj:`str`,optional)
      Name of a client side callback function, see JSONP.
    facet (:obj:`str`,optional)
      A name of an individual field or a comma separated list of fields

  Returns: :obj:`dict`
    Response

  References:
    1. https://pro.europeana.eu/page/search

  
  """
  params = {
      'wskey':get_api_key(),
      'query':kwargs.get('query','*'), 
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

  endpoint = 'https://api.europeana.eu/record/v2/search.json'

  if not kwargs:
    raise ValueError('No arguments passed')

  # test key
  response = requests.get(endpoint, params = {'wskey':params['wskey'],'query':'*'}).json()
  if not response['success']:
    raise ValueError(response['error'])

  # Necessary for handling facets of the type 'PROVIDER&f.PROVIDER.facet.limit=30&f.PROVIDER.facet.offset=10'
  _params = params.copy()
  if params['facet']:
    facet_list = params['facet'].split('&')
    if len(facet_list)>1:
      _params.update({'facet':facet_list[0]})
      _params.update({item.split('=')[0]:item.split('=')[1] for item in facet_list[1:]})

  url = requests.get(endpoint, params = _params).url
  response =  cursor_search(endpoint,_params)
  response.update({'url':url,'params':params})
  return response  
 



