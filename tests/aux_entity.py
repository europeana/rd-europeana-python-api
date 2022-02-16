import pyeuropeana.apis as apis
import os

if __name__ == '__main__':

    #entity_api = EntityAPI('wrong_key')

    resp = apis.entity.suggest(
        text = 'leonardo',
        TYPE = 'agent',
        language = 'es'
    )

    print(resp)

    resp = apis.entity.retrieve(
        TYPE = 'agent',
        IDENTIFIER = 2
    )

    print(resp)

    resp = apis.entity.resolve('http://dbpedia.org/resource/Leonardo_da_Vinci')


    print(resp)

    #API_KEY = os.environ.get('API_KEY')
    #print(API_KEY)

    # resp = entity_api.retrieve(
    #     TYPE = 'agent',
    #     IDENTIFIER = 25980
    # )

    # print(resp)

    # resp = entity_api.resolve('http://dbpedia.org/resource/Leonardo_da_Vinc')

    # print(resp)

