import fire
from time import time
from pathlib import Path
import pandas as pd


from pyeuropeana.apis import Search, Record
from pyeuropeana.utils import download_images, europeana_id2filename, url2img, resp2df

search_api = Search('api2demo')

n_objects = 200

response = search_api(
    query = 'PROVIDER:"German Digital Library"',
    profile = 'facets',
    facet = 'DATA_PROVIDER',
    rows = n_objects
)

print(response.keys())
print(len(response['items']))
print(response['url'])

df = resp2df(response)

facets = response['facets'][0]['fields']
print(facets)
