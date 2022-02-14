from pyeuropeana.apis import IIIFAPI


if __name__ == '__main__':

    IIIF_api = IIIFAPI('api2demo')

    resp = IIIF_api.manifest('/9200356/BibliographicResource_3000118390149')
    print(resp.keys())

    resp = IIIF_api.annopage(
        RECORD_ID = '/9200396/BibliographicResource_3000118436165', 
        PAGE_ID = 1
        )
    print(resp.keys())


    resp = IIIF_api.fulltext(
        RECORD_ID = '/9200396/BibliographicResource_3000118435063', 
        FULLTEXT_ID = '8ebb67ccf9f8a1dcc2ea119c60954111'
        )
    print(resp.keys())

    

    



    