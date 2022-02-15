from pyeuropeana.apis import SearchWrapper

if __name__ == '__main__':

    resp = SearchWrapper(
        wskey = 'api2demo',
        query = '*',
        )

    print(resp)



