import requests

class Record:
  def __init__(self,wskey):
    self.wskey = wskey
  def __call__(self,id):
    params = {'wskey':self.wskey}
    return requests.get(f'https://api.europeana.eu/record/v2/{id}.json',params=params).json()  
