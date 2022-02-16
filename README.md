# Python interface for Europeana's APIs

This package is a Python wrapper for Europeana's [Search](https://pro.europeana.eu/page/search) and [Record](https://pro.europeana.eu/page/record) APIs.

## Installation

As this package is not published on PyPI currently, the only way to install it is through its Git repository host using pip:

`pip install https://github.com/europeana/rd-europeana-python-api/archive/stable.zip`

From source

`git clone https://github.com/europeana/rd-europeana-python-api.git`

`cd rd-europeana-python-api`

`pip install -e .`

## Authentication

Get your API key [here](https://pro.europeana.eu/pages/get-api)

Set `EUROPEANA_API_KEY` as an environment variable running `export EUROPEANA_API_KEY=yourapikey` in the terminal.

If running in Google Colab use `os.environ['EUROPEANA_API_KEY'] = 'yourapikey'`

## Usage


```python
from pyeuropeana.apis import SearchWrapper
from pyeuropeana.utils.edm_utils import res2df

result = SearchWrapper(
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
dataframe = res2df(result, full=False)
```

[Colab tutorial](https://colab.research.google.com/drive/1VZJn9JKqziSF2jVQz1HRsvgbUZ0FM7qD?usp=sharing)
