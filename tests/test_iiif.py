import pyeuropeana.utils as utils
import pyeuropeana.apis as apis


if __name__ == "__main__":

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

    resp = apis.iiif.search(
    query = 'leonardo',
    profile = 'hits',
    rows = 250
    )

    print(len(resp['items']))

    resp = apis.iiif.search(
    query = 'leonardo',
    profile = 'hits&hit.selectors=5',
    rows = 250
    )

    print(resp['hits'])





    # result = apis.search(
    #     query = '*',
    #     qf = '(skos_concept:"http://data.europeana.eu/concept/base/48" AND TYPE:IMAGE)',
    #     reusability = 'open AND permission',
    #     media = True,
    #     thumbnail = True,
    #     landingpage = True,
    #     colourpalette = '#0000FF',
    #     theme = 'photography',
    #     sort = 'europeana_id',
    #     profile = 'rich',
    #     rows = 1000,
    #     ) # this gives you full response metadata along with cultural heritage object metadata

    #     # use this utility function to transform a subset of the cultural heritage object metadata
    #     # into a readable Pandas DataFrame
    # dataframe = utils.edm_utils.resp2df(result)