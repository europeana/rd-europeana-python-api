from PIL import Image
import pandas as pd
import urllib.request as urllibrec

from multiprocessing import Process, Manager
from pathlib import Path

def europeana_id2filename(europeana_id):
  return europeana_id.replace("/","11placeholder11")+'.jpg'

def europeana_id2uri(ID):
  return 'http://data.europeana.eu/item'+ID

def url2img(url):
    try:
        return Image.open(urllibrec.urlopen(url)).convert('RGB')
    except:
        print('Failed to get image')
        return None

def resp2df(response, full = False):
    if not response['items']:
        return None
    if full:
        return pd.json_normalize(response['items'])
    obj_list = [process_CHO_search(obj) for obj in response['items']]
    columns = [k for k in list(obj_list[0].keys()) if k not in ['raw_metadata']]
    return pd.DataFrame(obj_list)[columns]

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

# download images

def download_images(df, saving_path,time_limit = 20):

    #saving_path = '/home/jcejudo/projects/apis'

    saving_path = Path(saving_path)
    saving_path.mkdir(exist_ok = True, parents=True)

    #metadata_path = Path(saving_path).joinpath('metadata.csv')

    #df.to_csv(metadata_path)


    def worker(image_url,data_dict):
        img = url2img(image_url)
        data_dict['image']  = img

    manager = Manager()
    data_dict = manager.dict()
    valid_df = pd.DataFrame()
    for i,row in df.iterrows():
        print(i)
        if not row['image_url']:
            continue

        action_process = Process(target=worker,args=(row['image_url'],data_dict))
        action_process.start()
        action_process.join(timeout=time_limit) 
        action_process.terminate()
        
        if 'image' not in data_dict.keys():
            continue

        img = data_dict['image']

        if not img:
            continue

        valid_df.append(row)

        europeana_id = row['europeana_id']

        fname = europeana_id2filename(europeana_id)
        fpath = saving_path.joinpath(fname)


        img.save(fpath)

    return valid_df

    #valid_df.to_csv(metadata_path)





