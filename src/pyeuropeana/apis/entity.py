import requests


class Entity():
  def __init__(self,wskey):
    self.wskey = wskey
  def suggest(self,**kwargs):
    TYPE = kwargs.get('TYPE')
    text = kwargs.get('text')
    return requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':self.wskey,'text':text,'type':TYPE}).json()
  def retrieve(self,**kwargs):
    TYPE = kwargs.get('TYPE')
    IDENTIFIER = kwargs.get('IDENTIFIER')
    return requests.get(f'https://api.europeana.eu/entity/{TYPE}/base/{IDENTIFIER}.json',params = {'wskey':self.wskey}).json()