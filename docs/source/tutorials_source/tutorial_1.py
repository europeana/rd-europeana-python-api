"""
Tutorial 1
===========================

Introduction to tutorial
"""

# %%
# Imports
# -------
#
# Import the Python frameworks we need for this tutorial.
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

# %%
# Search API
# -----------
#

response =  apis.search(
    query = 'Leiden',
    qf = 'TYPE:IMAGE',
    rows = 250
)

df = utils.search2df(response['items'])

print(df.columns)
