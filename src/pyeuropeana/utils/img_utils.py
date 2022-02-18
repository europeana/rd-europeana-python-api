from pathlib import Path
from multiprocessing import Process, Manager
import urllib.request as urllibrec

import pandas as pd
from PIL import Image
from pyeuropeana.utils.edm_utils import europeana_id2filename

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



