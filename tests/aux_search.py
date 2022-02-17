import pyeuropeana.utils as utils
import pyeuropeana.apis as apis

if __name__ == "__main__":


    # Search
    apis.search(
    query = 'leonardo',
    rows = 150
    )

    # Record
    apis.record('/79/resource_document_museumboerhaave_V35167')

    # Entity
    apis.entity.suggest(
    text = 'leonardo',
    TYPE = 'agent',
    language = 'es'
    )
    apis.entity.retrieve(
    TYPE = 'agent',
    IDENTIFIER = 3
    )
    apis.entity.resolve('http://dbpedia.org/resource/Leonardo_da_Vinci')

    # IIIF
    apis.iiif.manifest('/9200356/BibliographicResource_3000118390149')
    apis.iiif.annopage(
    RECORD_ID = '/9200356/BibliographicResource_3000118390149',
    PAGE_ID = 1
    )
    apis.iiif.fulltext(
    RECORD_ID = '/9200396/BibliographicResource_3000118435063',
    FULLTEXT_ID = '8ebb67ccf9f8a1dcc2ea119c60954111'
    )

    resp = apis.search(
    query = 'leonardo',
    rows = 150
    )

    df = utils.edm_utils.resp2df(resp)