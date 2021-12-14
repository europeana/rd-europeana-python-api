import fire
from time import time
from pathlib import Path

from pyeuropeana.apis import Search, Record
from pyeuropeana.utils import download_images, europeana_id2filename, url2img

def main(**kwargs):

    # python pyeuropeana/tests.py --api_key api2demo --saving_path /home/jcejudo/projects/apis

    api_key = kwargs.get('api_key')
    saving_path = kwargs.get('saving_path')
    test_record = kwargs.get('test_record',False)
    n_objects = kwargs.get('n_objects',100)


    search_api = Search(api_key)
    record_api = Record(api_key)

    print('testing search api...')

    start = time()

    # Search API
    df = search_api(
        query = '*',
        qf = 'TYPE:IMAGE',
        rows = n_objects
    ).dataframe()

    d = time() - start
    print(d,'seconds')

    if test_record:
        # Record API

        print('testing record api...')

        start = time()

        for id in df['europeana_id'].values:
            record_response = record_api(id)

        d = time() - start
        print(d,'seconds')

    if saving_path:

        # Downloading image dataset

        print('downloading images...')

        start = time()

        download_images(df,saving_path)

        d = time() - start
        print(d,'seconds')

if __name__ == "__main__":
    fire.Fire(main)