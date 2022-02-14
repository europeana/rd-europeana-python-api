from pyeuropeana.apis import EntityAPI


if __name__ == '__main__':

    entity_api = EntityAPI('wrong_key')

    resp = entity_api.retrieve(
        text = 'leonardo',
        TYPE = 'agent',
        language = 'es'
    )

    print(resp)

    # resp = entity_api.retrieve(
    #     TYPE = 'agent',
    #     IDENTIFIER = 25980
    # )

    # print(resp)

    # resp = entity_api.resolve('http://dbpedia.org/resource/Leonardo_da_Vinc')

    # print(resp)

