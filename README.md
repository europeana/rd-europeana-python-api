# Python interface for Europeana's APIs

This package is a Python wrapper for Europeana's [Search](https://pro.europeana.eu/page/search) and [Record](https://pro.europeana.eu/page/record) APIs.

## Installation

As this package is not published on PyPI currently, the only way to install it is through its Git repository host using pip:

`pip install https://github.com/europeana/rd-europeana-python-api/archive/stable.zip`

From source

`git clone https://github.com/europeana/rd-europeana-python-api.git`

`cd rd-europeana-python-api`

`pip install -e .`



## Usage

Get your API key [here](https://pro.europeana.eu/pages/get-api)

```python
from pyeuropeana.apis import Search

search_api = Search('YOUR_API_KEY')

result = search_api(
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
