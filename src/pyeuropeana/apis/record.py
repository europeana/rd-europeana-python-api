import requests
import re

from ..utils.auth import get_api_key

def record(record_id):
  """
  Wrapper for the Record API [1]. Returns the information of an object specified by the Europeana ID

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.record('/79/resource_document_museumboerhaave_V35167')
  
  Args:
    record_id (:obj:`str`)
        The identifier of the record which is composed of the dataset identifier \\
        plus a local identifier within the dataset in the form of "/DATASET_ID/LOCAL_ID", for more detail see Europeana ID [2]

  Returns: :obj:`dict`
    Response


  References:
    1. https://pro.europeana.eu/page/record
    2. https://pro.europeana.eu/page/intro#identifying-records
  """

  params = {
    'wskey':get_api_key(),
    }
  
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
 
