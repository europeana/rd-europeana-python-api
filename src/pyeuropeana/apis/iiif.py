import requests
import re

from ..utils.auth import get_api_key

def manifest(RECORD_ID):
  """
  
  Manifest method of the IIIF API [1]. Returns a minimal set of metadata for an object

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.iiif.manifest('/9200356/BibliographicResource_3000118390149')
  
  Args:
    record_id (:obj:`str`)
        The identifier of the record which is composed of the dataset identifier \\
        plus a local identifier within the dataset in the form of "/DATASET_ID/LOCAL_ID", for more detail see Europeana ID [2]

  Returns :obj:`dict`
    Response

  References:
    1. https://pro.europeana.eu/page/iiif
  """
  wskey = get_api_key()
  europeana_id = re.findall('/\w*/\w*',RECORD_ID)
  if not europeana_id:
    raise ValueError('Not valid RECORD_ID')
  return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/manifest',params = {'wskey':wskey}).json()

def annopage(**kwargs):
  """
  Annopage method of the IIIF API [1]. Returns text and annotations for a given page of an object

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.iiif.annopage(
  >>>    RECORD_ID = '/9200356/BibliographicResource_3000118390149',
  >>>    PAGE_ID = 1,
  >>> )
  
  Args:
    RECORD_ID (:obj:`str`)
        The identifier of the record which is composed of the dataset identifier \\
        plus a local identifier within the dataset in the form of "/DATASET_ID/LOCAL_ID", for more detail see Europeana ID [2]
    PAGE_ID (:obj:`int`)
        The number of the page in logical sequence starting with 1 for the first page. 
        There can be pages that do not contain any text which will mean that the request will return a HTTP 404.

  Returns :obj:`dict`
    Response

  References:
    1. https://pro.europeana.eu/page/iiif
  """
  wskey = get_api_key()
  RECORD_ID = kwargs.get('RECORD_ID')
  PAGE_ID = kwargs.get('PAGE_ID')
  if not kwargs:
    raise ValueError('No arguments passed')
  europeana_id = re.findall('/\w*/\w*',RECORD_ID)
  if not europeana_id:
    raise ValueError('Not valid RECORD_ID')
  if not isinstance(PAGE_ID,int):
      raise ValueError('PAGE_ID must be an int')
  return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/annopage/{PAGE_ID}',params = {'wskey':wskey}).json()

def fulltext(**kwargs):
  """
  Fulltext method of the IIIF API [1]. Returns the transciption of a single page of a newspaper

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.iiif.fulltext(
  >>>    RECORD_ID = '/9200356/BibliographicResource_3000118390149',
  >>>    FULLTEXT_ID = '',
  >>> )
  
  Args:
    RECORD_ID (:obj:`str`)
        The identifier of the record which is composed of the dataset identifier \\
        plus a local identifier within the dataset in the form of "/DATASET_ID/LOCAL_ID", for more detail see Europeana ID [2]
    FULLTEXT_ID (:obj:`str`)
        The identifier of the full text resource.

  Returns :obj:`dict`
    Response

  References:
    1. https://pro.europeana.eu/page/iiif
  """
  wskey = get_api_key()
  RECORD_ID = kwargs.get('RECORD_ID')
  FULLTEXT_ID = kwargs.get('FULLTEXT_ID')
  if not kwargs:
    raise ValueError('No arguments passed')
  europeana_id = re.findall('/\w*/\w*',RECORD_ID)
  if not europeana_id:
    raise ValueError('Not valid RECORD_ID')
  return requests.get(f'https://www.europeana.eu/api/fulltext{RECORD_ID}/{FULLTEXT_ID}',params = {'wskey':wskey}).json()



def search(**kwargs):

  """
  Search method of the IIIF API [1]. Allows to search newspapers by their text content

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.iiif.search(
  >>>    query = 'Paris',
  >>>    profile = 'hits',
  >>> )
  
  Args:
    query (:obj:`str`)
        The term to search
    profile (:obj:`str`)
        If profile is 'hits' the mentions in the transcribed text where the search keyword was found will be displayed

  Returns :obj:`dict`
    Response

  References:
    1. https://pro.europeana.eu/page/iiif
  """

  params = {
      'wskey':get_api_key(),
      'query':kwargs.get('query','*'), 
      'profile':kwargs.get('profile'),
  }

  if not kwargs:
    raise ValueError('No arguments passed')

  response = requests.get('https://newspapers.eanadev.org/api/v2/search.json', params = params)
  url = response.url
  response = response.json()
  response.update({'url':url})
  return response



