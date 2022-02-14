from pyeuropeana.apis.apis import Search, Record
from pyeuropeana.utils.utils import resp2df

if __name__ == "__main__":

    search_api = Search('api2demo')

    n_objects = 200

    response = search_api(
        query = 'PROVIDER:"German Digital Library"',
        profile = 'facets',
        facet = 'DATA_PROVIDER',
        rows = n_objects
    )

    df = resp2df(response)

    facets = response['facets'][0]['fields']
    print(facets)
