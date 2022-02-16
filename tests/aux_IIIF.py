import pyeuropeana.apis as apis

if __name__ == '__main__':


    resp = apis.iiif.manifest('/9200356/BibliographicResource_3000118390149')
    print(resp.keys())

    resp = apis.iiif.annopage(
        RECORD_ID = '/9200396/BibliographicResource_3000118436165', 
        PAGE_ID = 1
        )
    print(resp.keys())

    resp = apis.iiif.fulltext(
        RECORD_ID = '/9200396/BibliographicResource_3000118435063', 
        FULLTEXT_ID = '8ebb67ccf9f8a1dcc2ea119c60954111'
        )
    print(resp.keys())

    

    



    