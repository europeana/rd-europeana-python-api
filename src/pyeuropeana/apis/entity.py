import requests

class EntityAPI:
  def __init__(self,wskey):
    self.wskey = wskey
    response = requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':self.wskey,'text':'leonardo','type':'agent'}).json()
    if 'success' in  response.items():
      raise ValueError(response['error'])
  def suggest(self,**kwargs):
    # to do: add language parameter
    
    TYPE = kwargs.get('TYPE')
    text = kwargs.get('text')
    if not kwargs:
      raise ValueError('No arguments passed')
    return requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':self.wskey,'text':text,'type':TYPE}).json()
  def retrieve(self,**kwargs):
    TYPE = kwargs.get('TYPE')
    IDENTIFIER = kwargs.get('IDENTIFIER')
    if not kwargs:
      raise ValueError('No arguments passed')
    return requests.get(f'https://api.europeana.eu/entity/{TYPE}/base/{IDENTIFIER}.json',params = {'wskey':self.wskey}).json()
