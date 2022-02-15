from pyeuropeana.apis import RecordWrapper

if __name__ == '__main__':

    resp = RecordWrapper(
        wskey = 'api2demo',
        #record_id = '/79/resource_document_museumboerhaave_V35167',
        record_id = 2
        )

    print(resp)



