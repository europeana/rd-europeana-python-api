# Python interface for Europeana's APIs

This package is a Python client library for [several APIs](https://pro.europeana.eu/page/apis) from [Europeana](https://pro.europeana.eu/):

* [Search API](https://pro.europeana.eu/page/search)
* [Record API](https://pro.europeana.eu/page/record)
* [Entity API](https://pro.europeana.eu/page/entity)
* [IIIF API](https://pro.europeana.eu/page/iiif)

With this tool you can access in python the data and metadata from our collections. Learn more about the Europeana Data Model [here](https://pro.europeana.eu/page/edm-documentation)

## Installation

### Using pip

`pip install pyeuropeana`

### From source

```
(.venv) $ git clone https://github.com/europeana/rd-europeana-python-api.git
(.venv) $ cd rd-europeana-python-api
(.venv) $ pip install .
```

## Authentication

Get your API key [here](https://pro.europeana.eu/pages/get-api)

Set `EUROPEANA_API_KEY` as an environment variable running `export EUROPEANA_API_KEY=yourapikey` in the terminal.

If running in Google Colab use `os.environ['EUROPEANA_API_KEY'] = 'yourapikey'`

## Usage

### [Search API](https://pro.europeana.eu/page/search)

```python
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

# use this function to search our collections
result = apis.search(
    query = '*',
    qf = '(skos_concept:"http://data.europeana.eu/concept/base/48" AND TYPE:IMAGE)',
    reusability = 'open AND permission',
    media = True,
    thumbnail = True,
    landingpage = True,
    colourpalette = '#0000FF',
    theme = 'photography',
    sort = 'europeana_id',
    profile = 'rich',
    rows = 1000,
    ) # this gives you full response metadata along with cultural heritage object metadata

    # use this utility function to transform a subset of the cultural heritage object metadata
    # into a readable Pandas DataFrame
dataframe = utils.edm_utils.resp2df(result)
```

### [Record API](https://pro.europeana.eu/page/record)

```python
import pyeuropeana.apis as apis

# gets the metadata from an object using its europeana id
data = apis.record('/79/resource_document_museumboerhaave_V35167')
```

### [Entity API](https://pro.europeana.eu/page/entity)

```python
import pyeuropeana.apis as apis

# suggests an entity based on a text query
data = apis.entity.suggest(
  text = 'leonardo',
  TYPE = 'agent',
  language = 'es'
)

# retrieves the data from an entity using the identifier
data = apis.entity.retrieve(
  TYPE = 'agent',
  IDENTIFIER = 3
)

# resolves entities from an input URI
data = apis.entity.resolve('http://dbpedia.org/resource/Leonardo_da_Vinci')
```

### [IIIF API](https://pro.europeana.eu/page/iiif)

```python
import pyeuropeana.apis as apis

# The IIIF API is mostly used to access newspapers collections at Europeana

# returns a minimal set of metadata for an object
data = apis.iiif.manifest('/9200356/BibliographicResource_3000118390149')

# returns text and annotations for a given page of an object
data = apis.iiif.annopage(
  RECORD_ID = '/9200356/BibliographicResource_3000118390149',
  PAGE_ID = 1
)

# returns the transciption of a single page of a newspaper
data = apis.iiif.fulltext(
  RECORD_ID = '/9200396/BibliographicResource_3000118435063',
  FULLTEXT_ID = '8ebb67ccf9f8a1dcc2ea119c60954111'
)

```

## Documentation

The documentation is available at [Read the Docs](https://rd-europeana-python-api.readthedocs.io/en/stable/apis.html)

You can also [build the docs](docs/README.md)

## Tutorials

[Colab tutorial](https://colab.research.google.com/drive/1VZJn9JKqziSF2jVQz1HRsvgbUZ0FM7qD?usp=sharing)
