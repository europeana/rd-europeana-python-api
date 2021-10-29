
import requests
from PIL import Image
import urllib.request as urllibrec
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd
import numpy as np

def europeana_id2filename(europeana_id):
  return europeana_id.replace("/","[ph]")+'.jpg'

def europeana_id2uri(ID):
  return 'http://data.europeana.eu/item'+ID


def showimg(img):
  fig,ax = plt.subplots()
  ax.imshow(img)
  ax.axis('off')
  plt.show()

def url2img(url):
    try:
        return Image.open(urllibrec.urlopen(url)).convert('RGB')
    except:
        print('Failed to get image')
        return None

def get_value_lang(lang_dict):
    if 'en' in lang_dict.keys():
      value = lang_dict['en']
    else:
      _ , value = list(lang_dict.items())[0]
    return value

def process_CHO_search(item):
  europeana_id = item['id'] if 'id' in item.keys() else None
  return {
      'raw_metadata': item,
      'europeana_id': europeana_id,
      'uri': europeana_id2uri(europeana_id),
      'type': item['type'] if 'type' in item.keys() else None,
      'image_url': item['edmIsShownBy'][0] if 'edmIsShownBy' in item.keys() else None,
      'country': item['country'][0] if 'country' in item.keys() else None,
      'description': item['dcDescription'][0] if 'dcDescription' in item.keys() else None,
      'title': item['title'][0] if 'title' in item.keys() else None,
      'creator': item['dcCreator'][0] if 'dcCreator' in item.keys() else None,
      'language': item['language'][0] if 'language' in item.keys() else None,
      'rights': item['rights'][0] if 'rights' in item.keys() else None,
      'provider': item['dataProvider'][0] if 'dataProvider' in item.keys() else None,
      'dataset_name': item['edmDatasetName'][0] if 'edmDatasetName' in item.keys() else None,
      'concept': item['edmConcept'][0] if 'edmConcept' in item.keys() else None,
      'concept_lang': {k:v[0] for k,v in item['edmConceptPrefLabelLangAware'].items()} if 'edmConceptPrefLabelLangAware' in item.keys() else None,
      'description_lang': {k:v[0] for k,v in item['dcDescriptionLangAware'].items()} if 'dcDescriptionLangAware' in item.keys() else None,
      'title_lang': {k:v[0] for k,v in item['dcTitleLangAware'].items()} if 'dcTitleLangAware' in item.keys() else None, 
  }


def process_CHO_record(response):
    obj = response['object']
    europeana_id = obj['about']

    try:
      image_url = obj['aggregations'][0]['edmIsShownBy']
    except:
      image_url = None

    # getting title
    proxy_list = obj['proxies']
    proxy_dict = {}
    for proxy in proxy_list:
      proxy_dict.update(proxy)

    title_lang = proxy_dict['dcTitle'] if 'dcTitle' in proxy_dict else None
    title = None
    if title_lang:
      title_lang = {k:v[0] for k,v in title_lang.items()}
      title = get_value_lang(title_lang)
      
    # getting provider
    provider_lang = obj['aggregations'][0]['edmProvider']
    provider_lang = {k:v[0] for k,v in provider_lang.items()}
    provider = get_value_lang(provider_lang)

    return {
        'raw_metadata': response,
        'europeana_id': europeana_id,
        'image_url': image_url,
        'uri': europeana_id2uri(europeana_id),
        'dataset_name': obj['edmDatasetName'][0],
        'country': obj['europeanaAggregation']['edmCountry']['def'][0],
        'language': obj['europeanaAggregation']['edmLanguage']['def'][0],
        'type': obj['type'],
        'title': title,
        'title_lang': title_lang,
        'rights': obj['aggregations'][0]['edmRights']['def'][0],
        'provider': provider,
        'provider_lang': provider_lang,
    }

def cursor_search(params):
    CHO_list = []
    response = {'nextCursor':'*'}
    while 'nextCursor' in response:
      if len(CHO_list)>params['rows']:
        break
      params.update({'cursor':response['nextCursor']})
      response = requests.get('https://api.europeana.eu/record/v2/search.json', params = params).json()  
      # to do: return if response is false
      CHO_list += response['items']
    return response, CHO_list[:params['rows']]

class SearchResponse:
  def __init__(self,**kwargs):
    self.CHO_list = kwargs.get('CHO_list')
    self.params = kwargs.get('params')
    self.response = kwargs.get('response')
  def dataframe(self):
    if not self.CHO_list:
      return None
    columns = [k for k in list(self.CHO_list[0].keys()) if k not in ['raw_metadata']]
    return pd.DataFrame(self.CHO_list)[columns]

class EuropeanaAPI:
  def __init__(self,wskey):
    self.wskey = wskey
  def search(self,**kwargs):
    params = {
        'wskey':self.wskey,
        'query':kwargs.get('query','*'), 
        'qf':kwargs.get('qf',''),
        'reusability':kwargs.get('reusability'),
        'media':kwargs.get('media'),
        'thumbnail':kwargs.get('thumbnail'),
        'landingpage':kwargs.get('landingpage'),
        'colourpalette':kwargs.get('colourpalette'),
        'theme':kwargs.get('theme'),
        'sort':kwargs.get('sort','random,europeana_id'),
        'profile':kwargs.get('profile'),
        'rows':kwargs.get('rows',12),
        'start':kwargs.get('start',1),
        'cursor':kwargs.get('cursor','*'),
        'callback':kwargs.get('callback'),        
    }
    response, CHO_list = cursor_search(params)
    return SearchResponse(
        CHO_list = [process_CHO_search(item) for item in CHO_list], 
        params = params,
        response = response,
        )
     
  def record(self,id):
    params = {'wskey':self.wskey}
    response = requests.get(f'https://api.europeana.eu/record/v2/{id}.json',params=params).json()  
    return process_CHO_record(response)
    


