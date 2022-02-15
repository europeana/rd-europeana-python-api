import requests
import re

def RecordWrapper(**kwargs):
  """
  Wrapper for the Record API

  Parameters
  ----------
  wskey : str
      The api key. Get an api key here (?)
  query : str
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
