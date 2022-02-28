from pathlib import Path
from multiprocessing import Process, Manager
import urllib.request as urllibrec

import pandas as pd
from PIL import Image
from pyeuropeana.utils.edm_utils import europeana_id2filename

def url2img(url,time_limit = 10):

    """
    Utility for obtaining a PIL Image object from an image url

    >>> import pyeuropeana.apis as apis
    >>> import pyeuropeana.utils as utils
    >>> resp = apis.search(
    >>>    query = 'Madrid',
    >>>    rows = 10,
    >>> )
    >>> df = utils.search2df(resp)
    >>> url = df['image_url'].values[0]
    >>> img = utils.url2img(url)

    Args:
      url (:obj:`str`)
        Image url

      time_limit (:obj:`int`, optional)
        Maximum time in seconds for getting the image, if longer the function returns None . Default is 10 seconds

    Returns: :obj:`PIL.Image`
      Image

    """

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
    if 'image' in data_dict.keys():
        return data_dict['image']
    else:
        return None



