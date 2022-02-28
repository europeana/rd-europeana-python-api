import urllib.request as urllibrec
from pathlib import Path
import pandas as pd
import requests

from typing import Optional

def search2df(response: dict, full: Optional[bool] = False) -> pd.DataFrame:
    """

    Utility for transforming the output of the search API into a dataframe

    >>> import pyeuropeana.apis as apis
    >>> import pyeuropeana.utils as utils
    >>> resp = apis.search(
    >>>    query = 'Rome',
    >>>    rows = 10,
    >>> )
    >>> df = utils.search2df(resp)

    Args:
      response (:obj:`dict`)
        Response from apis.search

      full (:obj:`bool`)
        Description

    Returns: :obj:`pd.DataFrame`
      Dataframe with columns ...

    """
    CHO_list = response['items']
    if not CHO_list:
        return None
    if full:
        return pd.json_normalize(CHO_list)
    CHO_list = [process_CHO_search(obj) for obj in CHO_list]
    return pd.DataFrame(CHO_list)


def cursor_search(endpoint,params):
  """
  Cursor search function
  """
  CHO_list = []
  response = {'nextCursor':params['cursor']}
  while 'nextCursor' in response:
    if len(CHO_list)>params['rows']:
      break
    params.update({'cursor':response['nextCursor']})
    response = requests.get(endpoint, params = params).json()
    CHO_list += response['items']
  CHO_list = CHO_list[:params['rows']]
  response['items'] = CHO_list
  return response


def europeana_id2uri(ID):
  return 'http://data.europeana.eu/item'+ID




def process_CHO_search(item):
  europeana_id = item['id'] if 'id' in item.keys() else None
  return {
      #'raw_metadata': item,
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
        #'raw_metadata': response,
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


def europeana_id2filename(europeana_id):
  return europeana_id.replace("/","[ph]")+'.jpg'

def get_value_lang(lang_dict):
    if 'en' in lang_dict.keys():
      value = lang_dict['en']
    else:
      _ , value = list(lang_dict.items())[0]
    return value

