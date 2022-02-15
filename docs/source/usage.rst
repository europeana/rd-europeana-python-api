Usage
=====

.. _installation:


Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

.. _quickstart:

Quickstart
------------

.. code-block:: python
    
    from pyeuropeana.apis import SearchWrapper
    from pyeuropeana.utils.edm_tools import resp2df
    
    resp = SearchWrapper(
        wskey = 'your key',
        query = 'Paris',
        rows = 150
    )

    df = resp2df(resp)














