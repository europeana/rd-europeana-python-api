from pathlib import Path
from multiprocessing import Process, Manager
import urllib.request as urllibrec

import pandas as pd
from PIL import Image
from pyeuropeana.utils.edm_utils import europeana_id2filename

# def _url2img(url):
#     try:
#         return Image.open(urllibrec.urlopen(url)).convert('RGB')
#     except:
#         #print('Failed to get image')
#         return None

def url2img(url,time_limit = 20):

    def worker(image_url,data_dict):
        try:
            data_dict['image']  = Image.open(urllibrec.urlopen(image_url)).convert('RGB')
        except:
            data_dict['image']  = None

    manager = Manager()
    data_dict = manager.dict()

    action_process = Process(target=worker,args=(url,data_dict))
    action_process.start()
    action_process.join(timeout=time_limit) 
    action_process.terminate()
    img = data_dict['image']
    return img



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