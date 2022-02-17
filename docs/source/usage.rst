Getting started
=====

.. _installation:

Installation
------------

Install the package using pip:

.. code-block:: console

   (.venv) $ pip install https://github.com/europeana/rd-europeana-python-api/archive/stable.zip

Or from source:

.. code-block:: console

   (.venv) $ git clone https://github.com/europeana/rd-europeana-python-api.git
   (.venv) $ cd rd-europeana-python-api
   (.venv) $ pip install .


.. _authentication:

Authentication
--------------

Obtain your API key here

Set `EUROPEANA_API_KEY` as an environment variable running

.. code-block:: console

   (.venv) $ export EUROPEANA_API_KEY=yourapikey

in the terminal.

You can also set it from python as

.. code-block:: python

   import os
   os.environ['EUROPEANA_API_KEY'] = 'yourapikey'


.. _quickstart:

Examples
------------

.. code-block:: python
    
    from pyeuropeana.apis import SearchWrapper
    from pyeuropeana.utils.edm_tools import resp2df
    
    resp = SearchWrapper(
        query = 'Paris',
        rows = 150
    )

    df = resp2df(resp)














