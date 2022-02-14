import requests
import re

class IIIFAPI:
  def __init__(self,wskey):
    self.wskey = wskey
    response = requests.get(f'https://iiif.europeana.eu/presentation/9200356/BibliographicResource_3000118390149/manifest',params = {'wskey':self.wskey}).json()
    if 'error' in  response.keys():
      raise ValueError(response['error'])

  def manifest(self,RECORD_ID):
    europeana_id = re.findall('/\w*/\w*',RECORD_ID)
    if not europeana_id:
      raise ValueError('Not valid RECORD_ID')
    return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/manifest',params = {'wskey':self.wskey}).json()

  def annopage(self,**kwargs):
    RECORD_ID = kwargs.get('RECORD_ID')
    PAGE_ID = kwargs.get('PAGE_ID')
    if not kwargs:
      raise ValueError('No arguments passed')
    europeana_id = re.findall('/\w*/\w*',RECORD_ID)
    if not europeana_id:
      raise ValueError('Not valid RECORD_ID')
    if not isinstance(PAGE_ID,int):
        raise ValueError('PAGE_ID must be an int')
    return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/annopage/{PAGE_ID}',params = {'wskey':self.wskey}).json()

  def fulltext(self,**kwargs):
    RECORD_ID = kwargs.get('RECORD_ID')
    FULLTEXT_ID = kwargs.get('FULLTEXT_ID')
    if not kwargs:
      raise ValueError('No arguments passed')
    europeana_id = re.findall('/\w*/\w*',RECORD_ID)
    if not europeana_id:
      raise ValueError('Not valid RECORD_ID')
    return requests.get(f'https://www.europeana.eu/api/fulltext{RECORD_ID}/{FULLTEXT_ID}',params = {'wskey':self.wskey}).json()



