import requests
import re

from ..utils.auth import get_api_key


# class IIIFAPI:
#   def __init__(self,wskey):
#     self.wskey = wskey
#     response = requests.get(f'https://iiif.europeana.eu/presentation/9200356/BibliographicResource_3000118390149/manifest',params = {'wskey':self.wskey}).json()
#     if 'error' in  response.keys():
#       raise ValueError(response['error'])

def manifest(RECORD_ID):
  """
  Wrapper for the IIIF API [1], method manifest

  >>> from pyeuropeana.apis import RecordWrapper
  >>> resp = RecordWrapper(
  >>>    record_id = '/79/resource_document_museumboerhaave_V35167',
  >>>     )
  
  Parameters
  ----------
  record_id : str
      The identifier of the record which is composed of the dataset identifier \\
      plus a local identifier within the dataset in the form of "/DATASET_ID/LOCAL_ID", for more detail see Europeana ID [2]

  References
    1. https://pro.europeana.eu/page/record
    2. https://pro.europeana.eu/page/intro#identifying-records
  """
  wskey = get_api_key()
  europeana_id = re.findall('/\w*/\w*',RECORD_ID)
  if not europeana_id:
    raise ValueError('Not valid RECORD_ID')
  return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/manifest',params = {'wskey':wskey}).json()

def annopage(**kwargs):
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
  wskey = get_api_key()
  RECORD_ID = kwargs.get('RECORD_ID')
  FULLTEXT_ID = kwargs.get('FULLTEXT_ID')
  if not kwargs:
    raise ValueError('No arguments passed')
  europeana_id = re.findall('/\w*/\w*',RECORD_ID)
  if not europeana_id:
    raise ValueError('Not valid RECORD_ID')
  return requests.get(f'https://www.europeana.eu/api/fulltext{RECORD_ID}/{FULLTEXT_ID}',params = {'wskey':wskey}).json()



