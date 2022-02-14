import requests

class IIIFAPI:
  def __init__(self,wskey):
    self.wskey = wskey
    response = requests.get(f'https://iiif.europeana.eu/presentation/9200356/BibliographicResource_3000118390149/manifest',params = {'wskey':self.wskey}).json()
    # if 'success' in  response.keys():
    #   raise ValueError(response['error'])

  def manifest(self,RECORD_ID):
    # to do: check for Record ID regex
    return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/manifest',params = {'wskey':self.wskey}).json()

  def annopage(self,**kwargs):
    # to do: add exceptions
    # to do: check for no args
    RECORD_ID = kwargs.get('RECORD_ID')
    PAGE_ID = kwargs.get('PAGE_ID')
    return requests.get(f'https://iiif.europeana.eu/presentation{RECORD_ID}/annopage/{PAGE_ID}',params = {'wskey':self.wskey}).json()

  def fulltext(self,**kwargs):
    # to do: add exceptions
    # to do: check for no args
    RECORD_ID = kwargs.get('RECORD_ID')
    FULLTEXT_ID = kwargs.get('FULLTEXT_ID')
    return requests.get(f'https://www.europeana.eu/api/fulltext{RECORD_ID}/{FULLTEXT_ID}',params = {'wskey':self.wskey}).json()



