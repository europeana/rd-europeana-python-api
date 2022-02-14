# from pyeuropeana.apis.apis import Search, Record
# from pyeuropeana.utils.utils import resp2df

import pyeuropeana.apis.search as search_api
import pyeuropeana.utils.edm_utils as edm_utils

if __name__ == "__main__":

    # test for wrong api key

    

    search_api = search_api.Search('api2demo2')

    n_objects = 200

    response = search_api(
        query = 'PROVIDER:"German Digital Library"',
        profile = 'facets',
        facet = 'DATA_PROVIDER',
        rows = n_objects
    )

    df = edm_utils.resp2df(response)

    facets = response['facets'][0]['fields']
    print(facets)
