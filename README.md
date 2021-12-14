# Python interface for Europeana's APIs

This package is a python wrapper for Europeana's [Search](https://pro.europeana.eu/page/search) and [Record](https://pro.europeana.eu/page/record) APIs


## Installation

Clone repository
```
git clone https://github.com/europeana/rd-europeana-python-api.git
cd rd-europeana-python-api
```
Install dependencies and package
```
pip install .

```

pip install https://github.com/europeana/rd-europeana-python-api/archive/testing.zip



## Usage

Get your API key [here](https://pro.europeana.eu/pages/get-api)

```
from pyeuropeana.apis import Search

search_api = Search('YOUR_API_KEY')

df = search_api(
  query = 'Rome',
  qf = '(skos_concept:"http://data.europeana.eu/concept/base/48" AND TYPE:IMAGE)'
  reusability = 'open',
  media = True,
  thumbnail = True,
  landingpage = True,
  colourpalette = '#0000FF',
  theme = 'photography',
  sort = 'random+asc',
  profile = 'rich',
  rows = 100,
  start = 1,
  cursor = '*',
  callback = None
).dataframe()


```

[Colab tutorial](https://colab.research.google.com/drive/1VZJn9JKqziSF2jVQz1HRsvgbUZ0FM7qD?usp=sharing)
