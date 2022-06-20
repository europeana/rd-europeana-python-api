.. note:: **You can download this tutorial in the .ipynb format or the .py format.**

  :download:`Download Python source code <tutorial_translation_files/tutorial_translation.py>`

  :download:`Download as Jupyter Notebook <tutorial_translation_files/tutorial_translation.ipynb>`

Translation Tutorial
====================


Introduction
------------

The `Europeana Foundation <https://www.europeana.eu/en>`__ digitally
collects currently more than 60 Millions Cultural Heritage (CH) records.
These records are described by a series of metadata that capture the
available information about the objects. For example the title, a text
that describes the object, the type of object (video, textual, etc) are
all relevant metadata.

One of the goals of Europeana is to improve the multilinguality of its
resources, meaning that as many records as possible should have
information available in as many languages are possible, ideally at
least all the 24 European languages. While many records are already
available in many languages, there are records that currently do not
hold yet relevant information in the language preferred by some of the
users of the Europeana platform. To tackle this problem, we could use an
automatic translation service to achieve a fuller language coverage of
the metadata.

This notebook contains a brief demo on using the `Europeana Search
API <https://pro.europeana.eu/page/search>`__ in combination with
`PyEuropeana <https://github.com/europeana/rd-europeana-python-api>`__,
a Python client library for Europeana APIs, to perform translations of
metadata and evaluate their quality. Read more about how the PyEuropeana
package works in the
`Documentation <https://rd-europeana-python-api.readthedocs.io/en/stable/>`__.

Importing packages
------------------

After installation of the missing packages we can import all needed
packages in the notebook

.. code:: python

    import pandas as pd
    import os
    from deep_translator import GoogleTranslator
    from nltk.translate.bleu_score import sentence_bleu
    pd.options.mode.chained_assignment = None
    import pyeuropeana.apis as apis
    import pyeuropeana.utils as utils
    import pyter

.. code:: python

    #setting enviroment variable
    os.environ['EUROPEANA_API_KEY'] = 'your_API_key' #replace with your API key

Definition of the translation function
--------------------------------------

In this section we define the function that will perform language
translation of a piece of text.

.. code:: python

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

Let us try if this function works on a simple piece of Dutch text to be
translated to English

.. code:: python

    text= "Hoe gaat het ?"
    translation=translate(text,'en')
    translation




.. parsed-literal::

    'How are you ?'



It looks like it is working!

In the following section we will be using the PyEuropeana module and the
Search API to query the Europeana database.

Querying the Europeana database
-------------------------------

Let us specify the query we want to execute and the number of CH records
that we would like to retrieve. The following query looks for the
records that have a description in Italian and asks to retrieve 10 of
them.

.. code:: python

    #Here we define the query and the number of record parameters
    query= 'proxy_dc_description.it:*'
    n_CH_records=10

Once we have defined the parameters we can perform the API call using
the apis module of the PyEuropeana package

.. code:: python

    response = apis.search(
        query = query,
        rows = n_CH_records,
        )

Let us take a look at the call response

.. code:: python

   #visualizing the first few objetcs
   dict(list(response.items())[0:5]) 



.. parsed-literal::

   {'apikey': 'api2demo',
 'success': True,
 'requestNumber': 999,
 'itemsCount': 10,
 'totalResults': 615910}


The response is a rich and complex JSON file, which is essentially a
list of nested dictionaries. The JSON format holds many different
metadata fields, for example ``itemCount`` and ``totalResults``. In many
cases we are not interested in all the metadata fields, but in a subset,
depending on the problem at hand. It is possible to visualize the full content of the file by typing ``response``.

It would then be useful if we could focus on a selection of the fields
and access them in an easier to read format than the JSON format, for
example a table. The PyEuropeana module offers just that!

Selection of a subset of metadata fields
----------------------------------------

Here we use the function ``search2df`` within the utils module of
PyEuropeana to select a predetermined subset of fields and cast them in
a tabular form

.. code:: python

    df_search=utils.search2df(response)
    df_search.columns




.. parsed-literal::

    Index(['europeana_id', 'uri', 'type', 'image_url', 'country', 'description',
           'title', 'creator', 'language', 'rights', 'provider', 'dataset_name',
           'concept', 'concept_lang', 'description_lang', 'title_lang'],
          dtype='object')



Comparing the names of the columns above with the original JSON file we
can notice that a subselection of fields has been performed by the
``search2df`` function. In the following section we will look to
translate the text in the ``description`` field, one of the most
important metadata fields.

Translations of the ``description`` field
-----------------------------------------

In this tutorial, the information we are interested in translating is
the description of the record, held in the ``description`` column. Let
us see if we can apply the function defined at the beginning of the
notebook to translate the description column from its original language,
Italian, to English.

We make a new column ``description_en`` and apply the function
``translate`` to the ``description`` column to translate it to English.

.. code:: python

    df_search['description_en']=df_search['description'].apply(translate,target='en')

Let us visualize only the original text and the English translation

.. code:: python

    #We select only the original description in Italian and its automatic translation to English
    df_translation=df_search[['description','description_en',]]
    df_translation




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>description</th>
          <th>description_en</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>Poster showing two geographical maps of Europe...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Poster showing in the center the geographical ...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster showing a map of north-eastern Italy an...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Manifesto che mostra al centro una carta geogr...</td>
          <td>Poster showing in the center a geographical ma...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster showing a map of north-eastern Italy an...</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster showing a map of Italy and the Balkans ...</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Manifesto che mostra la carta geografica del m...</td>
          <td>Poster showing the geographical map of the wor...</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Manifesto che mostra una rappresentazione geog...</td>
          <td>Poster showing a geographic representation of ...</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Manifesto che raffigura in azzurro la catena d...</td>
          <td>Poster depicting in blue the mountain range an...</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Manifesto che mostra la carta geograficha dell...</td>
          <td>Poster showing the geographical map of Venice ...</td>
        </tr>
      </tbody>
    </table>
    </div>



We get an idea by scanning the table above, and we can zoom in, for
example on the second row, to fully visualize the original text and its
translation.

.. code:: python

     list(df_translation.loc[1])




.. parsed-literal::

    ["Manifesto che mostra al centro la carta geografica dell'Italia in cui sono indicati i luoghi dove la Croce rossa americana è presente sul territorio,  intorno fanno da cornice alcune fotografie che documentano il lavoro svolto dalla Croce rossa americana, in alto sono presenti i ritratti fotografici di Woodrow Wilson, Robert Perkins ed Henry P. Davison.",
     'Poster showing in the center the geographical map of Italy showing the places where the American Red Cross is present in the area, around it are some photographs documenting the work done by the American Red Cross, at the top there are photographic portraits by Woodrow Wilson, Robert Perkins and Henry P. Davison.']



To a reader that understands both Italian and English the translation
looks ok, but can we take advantage of a quantitative metrics to measure
the quality of the translations?

Quality of translations
-----------------------

The next question we may ask is, can we measure the quality of these
metadata translations? The standard way to measure the quality of
translations is to compare them to reference translations and measure
how close the reference is to the automatic translation. Over time, many
metrics have been developed to do so, some of the most popular are
bilingual evaluation understudy,
(`BLEU <https://en.wikipedia.org/wiki/BLEU>`__) and translation error
rate
(`TER <https://kantanmtblog.com/2015/07/28/what-is-translation-error-rate-ter/>`__).
In our case, we don’t have reference translations at hand, therefore we
opt for the following: we translate back the English text into Italian,
and we measure how close the original Italian is to the back translated
Italian text. In essence we are using the original text in Italian as a
reference. We can then apply the scoring methods comparing the back
translation in Italian to the original text in Italian, assumed here as
reference. We can subsequently use this score as an estimate of the
quality of the initial translation from Italian to English. This method
that uses the back translation, to Italian in this case, is called round
trip translation
(`RTT <https://en.wikipedia.org/wiki/Round-trip_translation>`__). RTT
involves a two step process, the forward translation and the back
translation, while we compare and score only the back translation.
Therefore, if an error is detected in the backtranslated text it is
difficult to know if the error occurred in the forward translation, in
the back translation, or in both. In addition it is possible to get a
good back translation from a bad forward translation. Nevertheless,
there is some indication that the technique is useful to judge the
quality of longer texts, but not on a sentence level. Although the
technique presents downsides it allows us to get started when reference
translations are not available, and when we are not familiar with the
target language. Therefore in this case, we are going to leverage RTT to
show examples of how to evaluate the quality of translations.

Let us thus add a new column to the dataframe, ``description_en_it``, to
hold the back translation of the ``description`` column from English to
Italian and perform the translation

.. code:: python

    df_search['description_en_it']=df_search['description_en'].apply(translate, target= 'it')
    df_search=df_search[['description','description_en','description_en_it']] # visualize only the needed columns
    df_search.head(2)# visualize only the first two rows




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>description</th>
          <th>description_en</th>
          <th>description_en_it</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>Poster showing two geographical maps of Europe...</td>
          <td>Manifesto raffigurante due carte geografiche d...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Poster showing in the center the geographical ...</td>
          <td>Manifesto che mostra al centro la carta geogra...</td>
        </tr>
      </tbody>
    </table>
    </div>



Now, let us visualize the original text in Italian and the back
translation to Italian

.. code:: python

    df_translation_test=df_search[['description','description_en_it']]
    df_translation_test




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>description</th>
          <th>description_en_it</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>Manifesto raffigurante due carte geografiche d...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Manifesto che mostra al centro la carta geogra...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia nord...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Manifesto che mostra al centro una carta geogr...</td>
          <td>Manifesto che mostra al centro una mappa geogr...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia nord...</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia e de...</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Manifesto che mostra la carta geografica del m...</td>
          <td>Il manifesto raffigurante la carta geografica ...</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Manifesto che mostra una rappresentazione geog...</td>
          <td>Poster raffigurante una rappresentazione geogr...</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Manifesto che raffigura in azzurro la catena d...</td>
          <td>Poster raffigurante in blu la catena montuosa ...</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Manifesto che mostra la carta geograficha dell...</td>
          <td>Poster raffigurante la carta geografica di Ven...</td>
        </tr>
      </tbody>
    </table>
    </div>



They look pretty similar but let us quantify our impressions by applying
the TER metrics, adding a column that holds the value for this metrics.

.. code:: python

    df_translation_test['TER_score']=df_translation_test.apply(lambda x: pyter.ter(x['description'].split( ), x['description_en_it'].split()), axis=1)

.. code:: python

    df_translation_test




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>description</th>
          <th>description_en_it</th>
          <th>TER_score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>Manifesto raffigurante due carte geografiche d...</td>
          <td>0.281250</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>0.312500</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia nord...</td>
          <td>0.200000</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Manifesto che mostra al centro una carta geogr...</td>
          <td>Manifesto che mostra al centro una mappa geogr...</td>
          <td>0.357143</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia nord...</td>
          <td>0.347826</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia e de...</td>
          <td>0.416667</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Manifesto che mostra la carta geografica del m...</td>
          <td>Il manifesto raffigurante la carta geografica ...</td>
          <td>0.358974</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Manifesto che mostra una rappresentazione geog...</td>
          <td>Poster raffigurante una rappresentazione geogr...</td>
          <td>0.250000</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Manifesto che raffigura in azzurro la catena d...</td>
          <td>Poster raffigurante in blu la catena montuosa ...</td>
          <td>0.300000</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Manifesto che mostra la carta geograficha dell...</td>
          <td>Poster raffigurante la carta geografica di Ven...</td>
          <td>0.307692</td>
        </tr>
      </tbody>
    </table>
    </div>



Let us also add a column that holds the value for the BLEU metrics

.. code:: python

    df_translation_test['BLEU_score']=df_translation_test.apply(lambda x: sentence_bleu([x['description'].split( )], x['description_en_it'].split()), axis=1)
    df_translation_test




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>description</th>
          <th>description_en_it</th>
          <th>TER_score</th>
          <th>BLEU_score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>Manifesto raffigurante due carte geografiche d...</td>
          <td>0.281250</td>
          <td>0.525714</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>0.312500</td>
          <td>0.512205</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia nord...</td>
          <td>0.200000</td>
          <td>0.774552</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Manifesto che mostra al centro una carta geogr...</td>
          <td>Manifesto che mostra al centro una mappa geogr...</td>
          <td>0.357143</td>
          <td>0.525368</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia nord...</td>
          <td>0.347826</td>
          <td>0.447579</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Manifesto che mostra una carta geografica dell...</td>
          <td>Poster raffigurante una mappa dell'Italia e de...</td>
          <td>0.416667</td>
          <td>0.465922</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Manifesto che mostra la carta geografica del m...</td>
          <td>Il manifesto raffigurante la carta geografica ...</td>
          <td>0.358974</td>
          <td>0.526555</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Manifesto che mostra una rappresentazione geog...</td>
          <td>Poster raffigurante una rappresentazione geogr...</td>
          <td>0.250000</td>
          <td>0.742527</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Manifesto che raffigura in azzurro la catena d...</td>
          <td>Poster raffigurante in blu la catena montuosa ...</td>
          <td>0.300000</td>
          <td>0.602640</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Manifesto che mostra la carta geograficha dell...</td>
          <td>Poster raffigurante la carta geografica di Ven...</td>
          <td>0.307692</td>
          <td>0.515889</td>
        </tr>
      </tbody>
    </table>
    </div>



The TER and BLEU scores are both useful in evaluating translation
quality but they are based on different ideas. The TER metrics measures
the amount of editing needed to bring the translation in line with the
original reference, the **lower** the TER score the better the quality
of the translation. The BLEU score counts the number of overlapping
n-grams between the reference and the candidate translation, the
**higher** the BLEU score the better the quality of the translation.
Given their different ways of measuring the quality of translations the
two metrics could give in principle different results. In this case the
two metrics are strongly correlated as it is shown below

.. code:: python

    #correlation between Ter and Bleu scores
    df_translation_test[['TER_score','BLEU_score']].corr()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>TER_score</th>
          <th>BLEU_score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>TER_score</th>
          <td>1.000000</td>
          <td>-0.844842</td>
        </tr>
        <tr>
          <th>BLEU_score</th>
          <td>-0.844842</td>
          <td>1.000000</td>
        </tr>
      </tbody>
    </table>
    </div>



As anticipated above, we could then use the values of the BLEU and TER
scores as an estimate of the quality of the translations from Italian to
English, taking into account the limitations of RTT.

Conclusions
-----------

In this tutorial we briefily covered the following topics - Introduction
to metadata fields describing a CH object - Importance of having
relevant metadata fields available in many languages - Use of the
PyEuropeana module in combination with the Search API to retrieve CH
objects with a description in Italian - Automatic translation from
Italian to English of the retrieved metadata describing the CH object -
Use of the RTT method in combination with the TER and BLEU score to
estimate the quality of the obtained translations
