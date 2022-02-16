import requests
from ..utils.auth import get_api_key

def suggest(**kwargs):
  """
  Suggest method

  """
  wskey = get_api_key()
  language = kwargs.get('language','en')
  TYPE = kwargs.get('TYPE')
  text = kwargs.get('text')
  if not kwargs:
    raise ValueError('No arguments passed')
  if not text:
    raise ValueError('Argument "text" is needed')
  return requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':wskey,'text':text,'type':TYPE,'language':language}).json()


def retrieve(**kwargs):
  """
  Retrieve method

  """
  wskey = get_api_key()
  TYPE = kwargs.get('TYPE')
  IDENTIFIER = kwargs.get('IDENTIFIER')
  if not kwargs:
    raise ValueError('No arguments passed')
  return requests.get(f'https://api.europeana.eu/entity/{TYPE}/base/{IDENTIFIER}.json',params = {'wskey':wskey}).json()

def resolve(uri):
  """
  Resolve method

  """
  wskey = get_api_key()
  if not isinstance(uri,str):
    raise ValueError('input uri must be a string')
  response = requests.get(f'https://api.europeana.eu/entity/resolve/',params = {'wskey':wskey,'uri':uri}).json()
  if 'success' in  response.keys():
    raise ValueError(response['error'])
  return response
   


class EntityAPI:
  def __init__(self,wskey):
    self.wskey = wskey
    response = requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':self.wskey,'text':'leonardo','type':'agent'}).json()
    if 'success' in  response.keys():
      raise ValueError(response['error'])

  def suggest(self,**kwargs):
    """
    Suggest method
    """
    language = kwargs.get('language','en')
    TYPE = kwargs.get('TYPE')
    text = kwargs.get('text')
    if not kwargs:
      raise ValueError('No arguments passed')
    if not text:
      raise ValueError('Argument "text" is needed')
    return requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':self.wskey,'text':text,'type':TYPE,'language':language}).json()

  def retrieve(self,**kwargs):
    # to do: add exceptions
    TYPE = kwargs.get('TYPE')
    IDENTIFIER = kwargs.get('IDENTIFIER')
    if not kwargs:
      raise ValueError('No arguments passed')
    return requests.get(f'https://api.europeana.eu/entity/{TYPE}/base/{IDENTIFIER}.json',params = {'wskey':self.wskey}).json()

  def resolve(self,uri):
    if not isinstance(uri,str):
      raise ValueError('input uri must be a string')
    response = requests.get(f'https://api.europeana.eu/entity/resolve/',params = {'wskey':self.wskey,'uri':uri}).json()
    if 'success' in  response.keys():
      raise ValueError(response['error'])
    return response

