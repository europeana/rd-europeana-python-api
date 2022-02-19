"""
Tutorial 2
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

suggest_resp = apis.entity.suggest(
    TYPE = 'agent',
    text = 'leonardo'
)
print(suggest_resp)
