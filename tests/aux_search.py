import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

#from pyeuropeana.apis import SearchWrapper

if __name__ == '__main__':

    resp = apis.search(
        wskey = 'api2demo',
        query = '*',
        )

    print(resp)



