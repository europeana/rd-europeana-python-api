import requests
import re

def RecordWrapper(**kwargs):
  """
  Wrapper for the Record API [1]

  >>> from pyeuropeana.apis import RecordWrapper
  >>> resp = RecordWrapper(
  >>>    wskey = 'your_api_key',
  >>>    record_id = '/79/resource_document_museumboerhaave_V35167',
  >>>     )
  
  Parameters
  ----------
  wskey : str
      The api key. Get an api key here [2]
  record_id : str
      The identifier of the record which is composed of the dataset identifier \\
      plus a local identifier within the dataset in the form of "/DATASET_ID/LOCAL_ID", for more detail see Europeana ID [3]

  References
    1. https://pro.europeana.eu/page/record
    2. https://pro.europeana.eu/pages/get-api
    3. https://pro.europeana.eu/page/intro#identifying-records
  """

  params = {
    'wskey':kwargs.get('wskey'),
    }
  
  record_id = kwargs.get('record_id')

  if not kwargs:
    raise ValueError('No arguments passed')

  if not isinstance(record_id,str):
    raise ValueError('the input id should be a string')

  # check regex europeana ID
  europeana_id = re.findall('/\w*/\w*',record_id)
  if not europeana_id:
    raise ValueError('Not valid Europeana id')

  response = requests.get(f'https://api.europeana.eu/record/v2/{record_id}.json',params=params).json()  
  if not response['success']:
    raise ValueError(response['error'])
  return response
 

class RecordAPI:
  def __init__(self,wskey):
    self.wskey = wskey
    example_id = '/79/resource_document_museumboerhaave_V35167'
    response = requests.get(f'https://api.europeana.eu/record/v2/{example_id}.json',params={'wskey':self.wskey}).json()  
    if not response['success']:
     raise ValueError(response['error'])
     
  def __call__(self,id):
    params = {'wskey':self.wskey}

    if not isinstance(id,str):
      raise ValueError('the input should be a string')

    # check regex europeana ID
    europeana_id = re.findall('/\w*/\w*',id)
    if not europeana_id:
      raise ValueError('Not valid Europeana id')

    response = requests.get(f'https://api.europeana.eu/record/v2/{id}.json',params=params).json()  
    if not response['success']:
      raise ValueError(response['error'])
    return response
