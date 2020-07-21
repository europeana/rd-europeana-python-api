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
pip install -r requirements.txt
python setup.py install
```


## Usage

Get your API key [here](https://pro.europeana.eu/pages/get-api)

```
from europeana.api import EuropeanaAPI 
eu = EuropeanaAPI('your_API_key')
r = eu.search('Amsterdam', n = 5, reusability = 'open',  media = True, sort = {'term':'score','order':'asc'})

if r.success:
  print('Total number of results: {}'.format(r.totalResults ))
```

## Documentation




```
from europeana.api import EuropeanaAPI 
eu = EuropeanaAPI('your_API_key')
help(eu.search)
help(eu.record)
```

[Demo](https://colab.research.google.com/drive/177gvZQbaQ-5ou_j32hnIrJBmYWHVgmob?usp=sharing)
