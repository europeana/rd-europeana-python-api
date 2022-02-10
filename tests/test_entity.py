from pyeuropeana.apis import Entity

if __name__ == '__main__':

    entiti_api = Entity('api2demo')

    resp = entiti_api.suggest(
        TYPE = 'agent',
        text = 'leonardo'
    )

    print(resp)

    resp = entiti_api.suggest(
        TYPE = 'agent',
        IDENTIFIER = 25980
    )

    print(resp)

