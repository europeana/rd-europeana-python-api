#!/usr/bin/env python
# coding: utf-8

# # Introduction

# The [Europeana Foundation](https://www.europeana.eu/en) digitally collects currently more than 60 Millions Cultural Heritage (CH) records. These records are described by a series of metadata that capture the available information about the objects. For example the title, a text that describes the object, the type of object (video, textual, etc) are all relevant metadata. 
# 
# One of the goals of  Europeana is to improve the multilinguality of its resources, meaning that as many records as possible should have information available in as many languages are possible, ideally at least all the 24 European languages.
# While many records are already available in many languages, there are records that currently do not hold  yet relevant information in the language preferred by some of the users of the Europeana platform. 
# To tackle this problem, we could use an automatic translation service to achieve a fuller language coverage of the metadata. 
# 
# 
# This notebook contains a brief demo on using the [Europeana Search API](https://pro.europeana.eu/page/search) in combination with [PyEuropeana](https://github.com/europeana/rd-europeana-python-api), a Python client library for Europeana APIs, to perform translations of metadata and evaluate their quality. Read more about how the PyEuropeana package works in the [Documentation](https://rd-europeana-python-api.readthedocs.io/en/stable/).

# # Importing packages

# After installation of the missing packages we can import all needed packages in the notebook

# In[1]:


import pandas as pd
import os
from deep_translator import GoogleTranslator
from nltk.translate.bleu_score import sentence_bleu
pd.options.mode.chained_assignment = None
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils
import pyter


# In[2]:


#setting enviroment variable
os.environ['EUROPEANA_API_KEY'] = 'your_API_key' #replace with your API key


# # Definition of the translation function

# In this section we define the function that will perform language translation of a piece of text.

# In[3]:


def translate(txt, target):
    ''' This function performs automatic translation leveraging deep_translator
        Parameters
        txt(string): text to be translated
        target (string) language tag of the target language, it takes ISO 639-1 language codes'''
    if type(txt)==str: 
        #Here we are using the GoogleTranslator library, defining a source language that is detected 
        #automatically and a target language we want the text to be translated to
        translated=GoogleTranslator(source='auto', target=target).translate(txt)
    else:
        translated= 'Provided text is not a string and cannot be translated'
    return translated


# Let us try if this function works on a simple piece of Dutch text to be translated to English

# In[4]:


text= "Hoe gaat het ?"
translation=translate(text,'en')
translation


# It looks like it is working!

# In the following section we will be using the PyEuropeana module and the Search API to query the Europeana database.

# # Querying the Europeana database

# Let us specify the query we want to execute and the number of CH records that we would like to retrieve. The following query looks for the records that have a description in Italian and asks to retrieve 10 of them.

# In[5]:


#Here we define the query and the number of record parameters
query= 'proxy_dc_description.it:*'
n_CH_records=10


# Once we have defined the parameters we can perform the API call using the apis module of the PyEuropeana package

# In[6]:


response = apis.search(
    query = query,
    rows = n_CH_records,
    )


# Let us take a look at the response

# In[38]:


dict(list(response.items())[1:5]) #visualizing the first few objetcs


# The response  is a rich and complex JSON file, which is essentially a list of nested dictionaries. The JSON format holds many different metadata fields, for example `itemCount` and `totalResults`. In many cases we are not interested in all the metadata fields, but in a subset, depending on the problem at hand.  It is possible to visualize the full content of the file by typing `response`.
# 
# It would then be  useful if we could focus on a selection of the fields and access them in an easier to read  format than the JSON format, for example a table. The PyEuropeana module offers just that!

# # Selection of a subset of metadata fields

# Here we use the function `search2df` within the utils module of PyEuropeana to select a  predetermined subset of  fields and cast them in a tabular form

# In[39]:


df_search=utils.search2df(response)
df_search.columns


# Comparing the names of the columns above with the original JSON file we can notice that  a subselection of fields has been performed by the `search2df` function.
# In the following section we will look to translate the text in the `description` field, one of the most important metadata fields.

# # Translations of the `description` field

# In this tutorial, the information we are interested in translating is the description of the record, held in the `description` column. Let us see if we can apply the function defined at the beginning of the notebook to translate the description column from its original language, Italian, to English.

# We make a new column `description_en` and apply the function `translate` to the `description` column to translate it to English.

# In[40]:


df_search['description_en']=df_search['description'].apply(translate,target='en')


# Let us visualize only the original text and  the  English translation

# In[41]:


#We select only the original description in Italian and its automatic translation to English
df_translation=df_search[['description','description_en',]]
df_translation


# We get an idea by scanning the table above, and we can zoom in, for example on the second row, to fully visualize the original text and its translation.

# In[42]:


list(df_translation.loc[1])


# To a reader that understands both Italian and English the translation looks ok, but can we take advantage of a quantitative metrics to measure the quality of the translations?

# # Quality of translations

# The next question we may ask is, can we measure the quality of these metadata translations? <br>
# The standard  way to measure the quality of translations is to compare them to reference translations and measure how close the reference is to the automatic translation. Over time, many metrics have been developed to do so,  some of the most popular are bilingual evaluation understudy, ([BLEU](https://en.wikipedia.org/wiki/BLEU))  and translation error rate ([TER](https://kantanmtblog.com/2015/07/28/what-is-translation-error-rate-ter/)). <br>
# In our case, we don't have reference translations at hand, therefore we opt for the following: we translate back the English text into Italian, and we measure how close the original Italian is to the back translated  Italian text. In essence we are using the original text in Italian as a reference. We can then apply the scoring methods comparing  the back translation in Italian to the original text in Italian, assumed here as reference. We can subsequently use this score as an estimate of the quality of the initial translation from Italian to English. This method that uses the back translation, to Italian in this case, is called round trip translation ([RTT](https://en.wikipedia.org/wiki/Round-trip_translation)). RTT involves a two step process, the forward translation and the back translation, while we compare and score only the back translation. Therefore, if an error is detected in the backtranslated text it is difficult  to know if the error occurred in the forward translation, in the back translation, or in both. In addition it is possible to get a good back translation from a bad forward translation. Nevertheless, there is some indication that the technique is useful to judge the quality of longer texts, but not on a sentence level. Although the technique presents downsides it allows us to get started when reference translations are not available, and when we are not familiar with the target language. Therefore in this case, we are going to leverage RTT to show examples of how to evaluate the quality of translations.

# Let us thus add a new column to the dataframe, `description_en_it`, to hold the back translation of the `description` column from English to Italian and perform the translation

# In[43]:


df_search['description_en_it']=df_search['description_en'].apply(translate, target= 'it')
df_search=df_search[['description','description_en','description_en_it']] # visualize only the needed columns
df_search.head(2)# visualize only the first two rows


# Now, let us visualize the original text in Italian and the back translation to Italian

# In[44]:


df_translation_test=df_search[['description','description_en_it']]
df_translation_test


# They look pretty similar but let us quantify our impressions by applying the TER metrics, adding a column that holds the value for this metrics.

# In[45]:


df_translation_test['TER_score']=df_translation_test.apply(lambda x: pyter.ter(x['description'].split( ), x['description_en_it'].split()), axis=1)


# In[46]:


df_translation_test


# Let us also add a column that holds the value for the BLEU metrics

# In[47]:


df_translation_test['BLEU_score']=df_translation_test.apply(lambda x: sentence_bleu([x['description'].split( )], x['description_en_it'].split()), axis=1)
df_translation_test


# The TER and BLEU scores are both useful in evaluating translation quality but they are based on different ideas.
# The TER metrics measures the amount of editing needed to bring the translation in line with the original reference, the **lower** the TER score the better the quality of the  translation. 
# The BLEU score counts the number of overlapping n-grams between the reference and the candidate translation, the **higher** the BLEU score the better the quality of the translation. Given their different ways of measuring the quality of translations the two metrics could give in principle different results. In this case the two metrics are strongly correlated as it is shown below

# In[48]:


#correlation between Ter and Bleu scores
df_translation_test[['TER_score','BLEU_score']].corr()


# As anticipated above, we could then use the values of the BLEU and TER scores as an estimate of the quality of the translations from Italian to English, taking into account the limitations of RTT.

# # Conclusions

# In this tutorial we briefily covered the following topics
# - Introduction to metadata fields describing a CH object
# - Importance of having relevant metadata fields available in many languages
# - Use of the PyEuropeana module in combination with the Search API to retrieve CH objects with a description in Italian
# - Automatic translation from Italian to English of the retrieved metadata describing the CH object
# - Use of the RTT method in combination with the TER and BLEU score to estimate the quality of the obtained translations
