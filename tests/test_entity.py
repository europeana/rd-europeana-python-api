from pyeuropeana.apis.entity import Entity

if __name__ == '__main__':

    entity_api = Entity('api2demo')

    resp = entity_api.suggest(
        TYPE = 'agent',
        text = 'leonardo'
    )

    print(resp)

    resp = entity_api.retrieve(
        TYPE = 'agent',
        IDENTIFIER = 25980
    )

    print(resp)

