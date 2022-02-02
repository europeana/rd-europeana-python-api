# Python interface for Europeana's APIs

This package is a Python wrapper for Europeana's [Search](https://pro.europeana.eu/page/search) and [Record](https://pro.europeana.eu/page/record) APIs.

## Installation

As this package is not published on PyPI currently, the only way to install it is through its Git repository host using pip:

`pip install https://github.com/europeana/rd-europeana-python-api/archive/master.zip`

## Usage

Get your API key [here](https://pro.europeana.eu/pages/get-api)

```python
from pyeuropeana.apis import Search

search_api = Search('YOUR_API_KEY')

df = search_api(
  query = 'Rome',
  qf = '(skos_concept:"http://data.europeana.eu/concept/base/48" AND TYPE:IMAGE)'
  reusability = 'open AND permission',
  media = True,
  thumbnail = True,
  landingpage = True,
  colourpalette = '#0000FF',
  theme = 'photography',
  sort = 'europeana_id',
  profile = 'rich',
  rows = 100,
  cursor = '*',
  callback = None
).dataframe()
```

[Colab tutorial](https://colab.research.google.com/drive/1VZJn9JKqziSF2jVQz1HRsvgbUZ0FM7qD?usp=sharing)
