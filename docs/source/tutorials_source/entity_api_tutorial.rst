.. note:: **You can download this tutorial in the .ipynb format or the .py format.**

  :download:`Download Python source code <entity_api_tutorial_files/entity_api_tutorial.py>`

  :download:`Download as Jupyter Notebook <entity_api_tutorial_files/entity_api_tutorial.ipynb>`

Entity API Tutorial
===================

In this tutorial you will learn how to use the `Entity
API <https://pro.europeana.eu/page/entity>`__, which offers information
about several type of entities: ``agent``, ``place``, ``concept`` and
``timespan``. These named entities are part of the Europeana Entity
Collection, a collection of entities in the context of Europeana
harvested from and linked to controlled vocabularies, such as ​Geonames,
Dbpedia and Wikidata.

The Entity API has three methods:

-  ``apis.entity.suggest``: returns entities of a certain type matching
   a text query

-  ``apis.entity.retrieve``: returns information about an individual
   entity of a certain type

-  ``apis.entity.resolve``: returns entities that match a query url

We will use
`PyEuropeana <https://github.com/europeana/rd-europeana-python-api>`__,
a Python client library for Europeana APIs. Read more about how the
package works in the
`Documentation <https://rd-europeana-python-api.readthedocs.io/en/stable/>`__.

Install PyEuropeana with pip:

.. code:: python

    pip install pyeuropeana

Europeana APIs require a key for authentication, find more information
on how to get your API key
`here <https://pro.europeana.eu/pages/get-api>`__. Once you obtain your
key you can set it as an environment variable using the ``os`` library:

.. code:: python

    import os
    os.environ['EUROPEANA_API_KEY'] = 'your_API_key'

.. code:: python

    
    import pandas as pd
    pd.set_option('display.max_colwidth', 15)
    
    import pyeuropeana.apis as apis

Agents
------

In this section we focus on the agent type of entities. We would like to
find out if there are agents that match some query. In the following
cell we import the ``apis`` module from ``pyeuropeana`` and call the
``suggest`` method, which returns a dictionary

.. code:: python

    
    resp = apis.entity.suggest(                     
       text = 'leonardo',
       TYPE = 'agent',
    )
    
    resp.keys()




.. parsed-literal::

    dict_keys(['@context', 'type', 'total', 'items'])



The response contains several fields. The field ``total`` represents the
number of entities matching our query

.. code:: python

    resp['total']




.. parsed-literal::

    10



The field ``items`` contains a list where each object represents an
entity, which are the results of the search

.. code:: python

    len(resp['items'])




.. parsed-literal::

    10



This list can be converted in a pandas DataFrame as follows:

.. code:: python

    df = pd.json_normalize(resp['items'])
    cols = df.columns.tolist()
    cols = cols[-2:]+cols[:-2]
    df = df[cols]

The resulting dataframe has several columns. The ``id`` column contain
the identifier for the entity. The columns starting with ``shownBy``
contain information about an illustration for a given entity. We can
discard this information if we want

.. code:: python

    rm_cols = [col for col in df.columns if 'isShownBy' in col]
    df = df.drop(columns=rm_cols)
    df.head()




.. raw:: html

    
      <div id="df-78039f55-a88c-47ea-88fd-101b31ebe240">
        <div class="colab-df-container">
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
          <th>prefLabel.en</th>
          <th>altLabel.en</th>
          <th>id</th>
          <th>type</th>
          <th>dateOfBirth</th>
          <th>dateOfDeath</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Leonardo da...</td>
          <td>[Leonardo d...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1452-04-15</td>
          <td>1519-05-02</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Leonardo Leo</td>
          <td>[Leo, Leona...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1694-08-05</td>
          <td>1744-10-31</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Leonardo Sc...</td>
          <td>[Sciascia, ...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1921-01-08</td>
          <td>1989-11-20</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Leonardo Pa...</td>
          <td>[Padura Fue...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1955</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Bruno Leona...</td>
          <td>[Gelber, Br...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1941-03-19</td>
          <td>NaN</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-78039f55-a88c-47ea-88fd-101b31ebe240')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-78039f55-a88c-47ea-88fd-101b31ebe240 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-78039f55-a88c-47ea-88fd-101b31ebe240');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




We have some information about several entities matching our query. What
other information can we obtain for these entities?

The method ``retrieve`` can be used to obtain more information about a
particular entity using its identifier. The ``id`` column in the table
above contains the uris of the different entities, where the identifier
is an integer located at the end of each entiry uri.

For example, for the entity *Leonardo da Vinci* with uri
http://data.europeana.eu/agent/base/146741 we can call ``retrieve`` as:

.. code:: python

    resp = apis.entity.retrieve(
       TYPE = 'agent',
       IDENTIFIER = 146741,
    )
    
    resp.keys()




.. parsed-literal::

    dict_keys(['@context', 'id', 'type', 'isShownBy', 'prefLabel', 'altLabel', 'dateOfBirth', 'end', 'dateOfDeath', 'placeOfBirth', 'placeOfDeath', 'biographicalInformation', 'identifier', 'sameAs'])



We observe that the response contains several fields, some of them not
present in the suggest method.

The field ``prefLabel`` contains a list of the name of the entity in
different languages. We can transform this list into a dataframe

.. code:: python

    def get_name_df(resp):
      lang_name_df = None
      if 'prefLabel' in resp.keys():
        lang_name_df = pd.DataFrame([{'language':lang,'name':name} for lang,name in resp['prefLabel'].items()])
      return lang_name_df
    
    lang_name_df = get_name_df(resp)
    lang_name_df.head()




.. raw:: html

    
      <div id="df-0ffe555f-eea1-4a1e-99cd-681343600ac2">
        <div class="colab-df-container">
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
          <th>language</th>
          <th>name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>ar</td>
          <td>ليوناردو دا...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>az</td>
          <td>Leonardo da...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>be</td>
          <td>Леанарда да...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>bg</td>
          <td>Леонардо да...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>bs</td>
          <td>Leonardo da...</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-0ffe555f-eea1-4a1e-99cd-681343600ac2')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-0ffe555f-eea1-4a1e-99cd-681343600ac2 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-0ffe555f-eea1-4a1e-99cd-681343600ac2');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




The field ``biographicalInformation`` can be useful to know more about
the biography of the agent in particular. This information is also
multilingual, and can be transformed into a pandas DataFrame

.. code:: python

    def get_biography_df(resp):
      bio_df = None
      if 'biographicalInformation' in resp.keys():
        bio_df = pd.DataFrame(resp['biographicalInformation'])
      return bio_df
    
    bio_df = get_biography_df(resp)
    bio_df.head()




.. raw:: html

    
      <div id="df-f233655d-8cfb-47f2-811a-9e33af1713ab">
        <div class="colab-df-container">
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
          <th>@language</th>
          <th>@value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>de</td>
          <td>Leonardo da...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>no</td>
          <td>Leonardo di...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>hi</td>
          <td>लिओनार्दो द...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>fi</td>
          <td>Leonardo di...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>be</td>
          <td>Леана́рда д...</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-f233655d-8cfb-47f2-811a-9e33af1713ab')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-f233655d-8cfb-47f2-811a-9e33af1713ab button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-f233655d-8cfb-47f2-811a-9e33af1713ab');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




We can access the biography in English for instance in the following way

.. code:: python

    bio_df['@value'].loc[bio_df['@language'] == 'en'].values[0]




.. parsed-literal::

    'Leonardo di ser Piero da Vinci (Italian pronunciation: [leoˈnardo da vˈvintʃi] About this sound pronunciation ; April 15, 1452 – May 2, 1519, Old Style) was an Italian Renaissance polymath: painter, sculptor, architect, musician, mathematician, engineer, inventor, anatomist, geologist, cartographer, botanist, and writer. His genius, perhaps more than that of any other figure, epitomized the Renaissance humanist ideal.Leonardo has often been described as the archetype of the Renaissance Man, a man of "unquenchable curiosity" and "feverishly inventive imagination". He is widely considered to be one of the greatest painters of all time and perhaps the most diversely talented person ever to have lived. According to art historian Helen Gardner, the scope and depth of his interests were without precedent and "his mind and personality seem to us superhuman, the man himself mysterious and remote". Marco Rosci states that while there is much speculation about Leonardo, his vision of the world is essentially logical rather than mysterious, and that the empirical methods he employed were unusual for his time.Born out of wedlock to a notary, Piero da Vinci, and a peasant woman, Caterina, in Vinci in the region of Florence, Leonardo was educated in the studio of the renowned Florentine painter Verrocchio. Much of his earlier working life was spent in the service of Ludovico il Moro in Milan. He later worked in Rome, Bologna and Venice, and he spent his last years in France at the home awarded him by Francis I.Leonardo was, and is, renowned primarily as a painter. Among his works, the Mona Lisa is the most famous and most parodied portrait and The Last Supper the most reproduced religious painting of all time, with their fame approached only by Michelangelo\'s The Creation of Adam. Leonardo\'s drawing of the Vitruvian Man is also regarded as a cultural icon, being reproduced on items as varied as the euro coin, textbooks, and T-shirts. Perhaps fifteen of his paintings have survived, the small number because of his constant, and frequently disastrous, experimentation with new techniques, and his chronic procrastination. Nevertheless, these few works, together with his notebooks, which contain drawings, scientific diagrams, and his thoughts on the nature of painting, compose a contribution to later generations of artists rivalled only by that of his contemporary, Michelangelo.Leonardo is revered for his technological ingenuity. He conceptualised flying machines, a tank, concentrated solar power, an adding machine, and the double hull, also outlining a rudimentary theory of plate tectonics. Relatively few of his designs were constructed or were even feasible during his lifetime, but some of his smaller inventions, such as an automated bobbin winder and a machine for testing the tensile strength of wire, entered the world of manufacturing unheralded. He made important discoveries in anatomy, civil engineering, optics, and hydrodynamics, but he did not publish his findings and they had no direct influence on later science.'



Now, let’s say that we want to find the biography for all the entities
returned by ``entity.search``. We can encapsulate the previous steps
into a function that can be applied to the DataFrame reulting from
``entity.search``:

.. code:: python

    def get_bio_uri(uri):
      id = int(uri.split('/')[-1])
      resp = apis.entity.retrieve(
        TYPE = 'agent',
        IDENTIFIER = id,
      )
    
      bio_df = get_biography_df(resp)
      bio = bio_df['@value'].loc[bio_df['@language'] == 'en'].values[0]
      return bio
    
    df['bio'] = df['id'].apply(get_bio_uri)
    df.head()




.. raw:: html

    
      <div id="df-9e258231-f4ff-4f5b-9dac-02befbd1422f">
        <div class="colab-df-container">
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
          <th>prefLabel.en</th>
          <th>altLabel.en</th>
          <th>id</th>
          <th>type</th>
          <th>dateOfBirth</th>
          <th>dateOfDeath</th>
          <th>bio</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Leonardo da...</td>
          <td>[Leonardo d...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1452-04-15</td>
          <td>1519-05-02</td>
          <td>Leonardo di...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Leonardo Leo</td>
          <td>[Leo, Leona...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1694-08-05</td>
          <td>1744-10-31</td>
          <td>Leonardo Le...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Leonardo Sc...</td>
          <td>[Sciascia, ...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1921-01-08</td>
          <td>1989-11-20</td>
          <td>Leonardo Sc...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Leonardo Pa...</td>
          <td>[Padura Fue...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1955</td>
          <td>NaN</td>
          <td>Leonardo Pa...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Bruno Leona...</td>
          <td>[Gelber, Br...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1941-03-19</td>
          <td>NaN</td>
          <td>Bruno Leona...</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-9e258231-f4ff-4f5b-9dac-02befbd1422f')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-9e258231-f4ff-4f5b-9dac-02befbd1422f button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-9e258231-f4ff-4f5b-9dac-02befbd1422f');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




The biography in English has been added for each entity. Great!

Something of interest can be the place of birth and death of the agents.
We can create a function as:

.. code:: python

    def get_place_resp(resp, event):
    
      if event == 'birth':
        if 'placeOfBirth' not in resp.keys():
          return
        place = resp['placeOfBirth']
    
      elif event == 'death':
        if 'placeOfDeath' not in resp.keys():
          return
        place = resp['placeOfDeath']
    
      if not place:
        return
    
      place = list(place[0].values())[0]
      
      if place.startswith('http'):
         place = place.split('/')[-1].replace('_',' ')
      return place
    
    
    
    resp = apis.entity.retrieve(
       TYPE = 'agent',
       IDENTIFIER = 146741,
    )
    get_place_resp(resp, 'birth')





.. parsed-literal::

    'Republic of Florence'



.. note::
  The function above parses the URI and extracts the name of the places of
  birth and date. In reality we should use either the ``resolve`` method
  of the Entity API, if the URI is that of an entity in Europeana’s Entity
  Collection, or seek to de-reference it using (Linked Data) `content
  negotiation <https://https://www.w3.org/DesignIssues/Conneg>`__, if it
  is not known in the Entity Collection.





Now we can add this information to the original DataFrame:

.. code:: python

    def get_place(uri,event):
      id = int(uri.split('/')[-1])
      resp = apis.entity.retrieve(
        TYPE = 'agent',
        IDENTIFIER = id,
      )
      return get_place_resp(resp,event)
    
    
    df['placeOfBirth'] = df['id'].apply(lambda x: get_place(x,'birth'))
    df['placeOfDeath'] = df['id'].apply(lambda x: get_place(x,'death'))
    df.head()
    





.. raw:: html

    
      <div id="df-e3849b93-8748-45cf-95db-4d8764263b32">
        <div class="colab-df-container">
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
          <th>prefLabel.en</th>
          <th>altLabel.en</th>
          <th>id</th>
          <th>type</th>
          <th>dateOfBirth</th>
          <th>dateOfDeath</th>
          <th>bio</th>
          <th>placeOfBirth</th>
          <th>placeOfDeath</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Leonardo da...</td>
          <td>[Leonardo d...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1452-04-15</td>
          <td>1519-05-02</td>
          <td>Leonardo di...</td>
          <td>Republic of...</td>
          <td>Kingdom of ...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Leonardo Leo</td>
          <td>[Leo, Leona...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1694-08-05</td>
          <td>1744-10-31</td>
          <td>Leonardo Le...</td>
          <td>None</td>
          <td>Naples</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Leonardo Sc...</td>
          <td>[Sciascia, ...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1921-01-08</td>
          <td>1989-11-20</td>
          <td>Leonardo Sc...</td>
          <td>Racalmuto</td>
          <td>Sicily</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Leonardo Pa...</td>
          <td>[Padura Fue...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1955</td>
          <td>NaN</td>
          <td>Leonardo Pa...</td>
          <td>Cuba</td>
          <td>None</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Bruno Leona...</td>
          <td>[Gelber, Br...</td>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1941-03-19</td>
          <td>NaN</td>
          <td>Bruno Leona...</td>
          <td>Buenos Aires</td>
          <td>None</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-e3849b93-8748-45cf-95db-4d8764263b32')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-e3849b93-8748-45cf-95db-4d8764263b32 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-e3849b93-8748-45cf-95db-4d8764263b32');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




The previous pipeline can be applied to any other agent:

.. code:: python

    resp = apis.entity.suggest(
       text = 'Marguerite Gérard',
       TYPE = 'agent',
    )
    
    df = pd.json_normalize(resp['items'])
    df = df.drop(columns=[col for col in df.columns if 'isShownBy' in col])
    df['bio'] = df['id'].apply(get_bio_uri)
    df['placeOfBirth'] = df['id'].apply(lambda x: get_place(x,'birth'))
    df['placeOfDeath'] = df['id'].apply(lambda x: get_place(x,'death'))
    df.head()
    





.. raw:: html

    
      <div id="df-83a3ff77-f2d4-4de6-84fe-c1e41104bcb3">
        <div class="colab-df-container">
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
          <th>id</th>
          <th>type</th>
          <th>dateOfBirth</th>
          <th>dateOfDeath</th>
          <th>prefLabel.en</th>
          <th>altLabel.en</th>
          <th>bio</th>
          <th>placeOfBirth</th>
          <th>placeOfDeath</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>http://data...</td>
          <td>Agent</td>
          <td>1761-01-28</td>
          <td>1837-05-18</td>
          <td>Marguerite ...</td>
          <td>[Marguerite...</td>
          <td>Marguerite ...</td>
          <td>France</td>
          <td>Paris</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-83a3ff77-f2d4-4de6-84fe-c1e41104bcb3')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-83a3ff77-f2d4-4de6-84fe-c1e41104bcb3 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-83a3ff77-f2d4-4de6-84fe-c1e41104bcb3');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




Finally, we can use the method ``resolve`` for obtaining the entity
matching a an external URI when it is present as entity in the Europeana
Entity Collection. Find more information `in the documentation of the
Entity API <https://pro.europeana.eu/page/entity#resolve>`__

.. code:: python

    resp = apis.entity.resolve('http://dbpedia.org/resource/Leonardo_da_Vinci')
    resp.keys()




.. parsed-literal::

    dict_keys(['@context', 'id', 'type', 'isShownBy', 'prefLabel', 'altLabel', 'dateOfBirth', 'end', 'dateOfDeath', 'placeOfBirth', 'placeOfDeath', 'biographicalInformation', 'identifier', 'sameAs'])



Places
------

One of the types of entities we can work with are places. Let’s get the
place of death of the previous agent

.. code:: python

    place_of_death = df['placeOfDeath'].values[0]
    place_of_death




.. parsed-literal::

    'Paris'



We can now search the entity corresponding to this place by using the
suggest method using ``place`` as the ``TYPE`` argument.

.. code:: python

    resp = apis.entity.suggest(
       text = place_of_death,
       TYPE = 'place',
    
    )
    place_df = pd.json_normalize(resp['items'])
    cols = place_df.columns.tolist()
    cols = cols[-1:]+cols[:-1]
    place_df = place_df[cols]
    place_df.head()




.. raw:: html

    
      <div id="df-7408b3f3-bc13-439d-a091-d480dd2cb51e">
        <div class="colab-df-container">
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
          <th>prefLabel.en</th>
          <th>id</th>
          <th>type</th>
          <th>isPartOf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Paris</td>
          <td>http://data...</td>
          <td>Place</td>
          <td>[{'id': 'ht...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>La Defense</td>
          <td>http://data...</td>
          <td>Place</td>
          <td>[{'id': 'ht...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Jõelähtme P...</td>
          <td>http://data...</td>
          <td>Place</td>
          <td>[{'id': 'ht...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Vihula Parish</td>
          <td>http://data...</td>
          <td>Place</td>
          <td>[{'id': 'ht...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Põlva Parish</td>
          <td>http://data...</td>
          <td>Place</td>
          <td>[{'id': 'ht...</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-7408b3f3-bc13-439d-a091-d480dd2cb51e')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-7408b3f3-bc13-439d-a091-d480dd2cb51e button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-7408b3f3-bc13-439d-a091-d480dd2cb51e');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




Let’s use the first uri with the ``retrieve`` method

.. code:: python

    uri = place_df['id'].values[0]
    IDENTIFIER = uri.split('/')[-1]
    
    resp = apis.entity.retrieve(
       IDENTIFIER = IDENTIFIER,
       TYPE = 'place',
    )
    resp.keys()




.. parsed-literal::

    dict_keys(['@context', 'id', 'type', 'prefLabel', 'altLabel', 'lat', 'long', 'isPartOf', 'sameAs'])



We can reuse the function ``get_name_df`` for places as well, as the
response has a similar data structure as for ``agent``

.. code:: python

    name_df = get_name_df(resp)
    name_df.head()




.. raw:: html

    
      <div id="df-7d2a3d74-f45e-480a-ac96-e030c143a0ac">
        <div class="colab-df-container">
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
          <th>language</th>
          <th>name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td></td>
          <td>Paris</td>
        </tr>
        <tr>
          <th>1</th>
          <td>de</td>
          <td>Paris</td>
        </tr>
        <tr>
          <th>2</th>
          <td>en</td>
          <td>Paris</td>
        </tr>
        <tr>
          <th>3</th>
          <td>es</td>
          <td>Paris</td>
        </tr>
        <tr>
          <th>4</th>
          <td>fr</td>
          <td>Paris</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-7d2a3d74-f45e-480a-ac96-e030c143a0ac')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-7d2a3d74-f45e-480a-ac96-e030c143a0ac button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-7d2a3d74-f45e-480a-ac96-e030c143a0ac');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




The response include the field ``isPartOf``, which indicates an entity
that the current entity belongs to, if any

.. code:: python

    is_part_uri = resp['isPartOf'][0]
    is_part_uri




.. parsed-literal::

    'http://data.europeana.eu/place/base/42377'



Let’s see what this misterious uri refers to using the retrieve method

.. code:: python

    is_part_id = is_part_uri.split('/')[-1]
    resp = apis.entity.retrieve(
       IDENTIFIER = is_part_id,
       TYPE = 'place',
    )
    
    name_df = get_name_df(resp)
    name_df.head()




.. raw:: html

    
      <div id="df-095f9725-053b-4526-9437-6daa2e73411b">
        <div class="colab-df-container">
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
          <th>language</th>
          <th>name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td></td>
          <td>Île-de-France</td>
        </tr>
        <tr>
          <th>1</th>
          <td>de</td>
          <td>Île-de-France</td>
        </tr>
        <tr>
          <th>2</th>
          <td>en</td>
          <td>Île-de-France</td>
        </tr>
        <tr>
          <th>3</th>
          <td>es</td>
          <td>Isla de Fra...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>fr</td>
          <td>Région pari...</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-095f9725-053b-4526-9437-6daa2e73411b')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-095f9725-053b-4526-9437-6daa2e73411b button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-095f9725-053b-4526-9437-6daa2e73411b');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




It had to be the emblematic *Île-de-France*, of course! And its
coordinates are:

.. code:: python

    f"lat: {resp['lat']}, long: {resp['long']}"




.. parsed-literal::

    'lat: 48.7, long: 2.5'



Concepts
--------

Let’s query for all concepts

.. code:: python

    resp = apis.entity.suggest(
       text = 'war',
       TYPE = 'concept',
    )
    
    resp['total']




.. parsed-literal::

    3



We build a table containing the field ``items``, were we can see the
name and uri of the different concepts

.. code:: python

    df = pd.json_normalize(resp['items'])
    df = df.drop(columns=[col for col in df.columns if 'isShownBy' in col])
    df.head()




.. raw:: html

    
      <div id="df-387f25ea-42f5-4725-b650-275c95365f56">
        <div class="colab-df-container">
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
          <th>id</th>
          <th>type</th>
          <th>prefLabel.en</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>http://data...</td>
          <td>Concept</td>
          <td>World War I</td>
        </tr>
        <tr>
          <th>1</th>
          <td>http://data...</td>
          <td>Concept</td>
          <td>War photogr...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>http://data...</td>
          <td>Concept</td>
          <td>Raku ware</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-387f25ea-42f5-4725-b650-275c95365f56')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-387f25ea-42f5-4725-b650-275c95365f56 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-387f25ea-42f5-4725-b650-275c95365f56');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




Do we want to know more information about the first concept of the list?
We got it

.. code:: python

    concept_uri = df['id'].values[0]
    concept_uri




.. parsed-literal::

    'http://data.europeana.eu/concept/base/83'



.. code:: python

    concept_id = concept_uri.split('/')[-1]
    resp = apis.entity.retrieve(
       IDENTIFIER = concept_id,
       TYPE = 'concept',
    )
    
    name_df = get_name_df(resp)
    name_df.loc[name_df['language'] == 'en']




.. raw:: html

    
      <div id="df-c09965a5-3c8f-4d2d-bf34-05192ced5e33">
        <div class="colab-df-container">
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
          <th>language</th>
          <th>name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>11</th>
          <td>en</td>
          <td>World War I</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-c09965a5-3c8f-4d2d-bf34-05192ced5e33')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-c09965a5-3c8f-4d2d-bf34-05192ced5e33 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-c09965a5-3c8f-4d2d-bf34-05192ced5e33');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




The concept is World War I. We can get some related concepts from
dbpedia

.. code:: python

    resp['related'][:5]




.. parsed-literal::

    ['http://dbpedia.org/resource/Category:Wars_involving_Nicaragua',
     'http://dbpedia.org/resource/Category:Wars_involving_the_United_Kingdom',
     'http://dbpedia.org/resource/Category:Wars_involving_Greece',
     'http://dbpedia.org/resource/Category:Wars_involving_Sri_Lanka',
     'http://dbpedia.org/resource/Category:Wars_involving_Czechoslovakia']



The field ``note`` contains a multilingual description of the concept

.. code:: python

    note_df = pd.json_normalize([{'lang':k,'note':v[0]} for k,v in resp['note'].items()])
    note_df.head()




.. raw:: html

    
      <div id="df-4f8f16ff-b0c9-4a5b-9386-97f5abe4c607">
        <div class="colab-df-container">
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
          <th>lang</th>
          <th>note</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>ar</td>
          <td>الحرب العال...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>az</td>
          <td>Birinci dün...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>be</td>
          <td>Першая сусв...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>bg</td>
          <td>Първата све...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>bs</td>
          <td>Prvi svjets...</td>
        </tr>
      </tbody>
    </table>
    </div>
          <button class="colab-df-convert" onclick="convertToInteractive('df-4f8f16ff-b0c9-4a5b-9386-97f5abe4c607')"
                  title="Convert this dataframe to an interactive table."
                  style="display:none;">
    
      <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
           width="24px">
        <path d="M0 0h24v24H0V0z" fill="none"/>
        <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
      </svg>
          </button>
    
      <style>
        .colab-df-container {
          display:flex;
          flex-wrap:wrap;
          gap: 12px;
        }
    
        .colab-df-convert {
          background-color: #E8F0FE;
          border: none;
          border-radius: 50%;
          cursor: pointer;
          display: none;
          fill: #1967D2;
          height: 32px;
          padding: 0 0 0 0;
          width: 32px;
        }
    
        .colab-df-convert:hover {
          background-color: #E2EBFA;
          box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
          fill: #174EA6;
        }
    
        [theme=dark] .colab-df-convert {
          background-color: #3B4455;
          fill: #D2E3FC;
        }
    
        [theme=dark] .colab-df-convert:hover {
          background-color: #434B5C;
          box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
          filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
          fill: #FFFFFF;
        }
      </style>
    
          <script>
            const buttonEl =
              document.querySelector('#df-4f8f16ff-b0c9-4a5b-9386-97f5abe4c607 button.colab-df-convert');
            buttonEl.style.display =
              google.colab.kernel.accessAllowed ? 'block' : 'none';
    
            async function convertToInteractive(key) {
              const element = document.querySelector('#df-4f8f16ff-b0c9-4a5b-9386-97f5abe4c607');
              const dataTable =
                await google.colab.kernel.invokeFunction('convertToInteractive',
                                                         [key], {});
              if (!dataTable) return;
    
              const docLinkHtml = 'Like what you see? Visit the ' +
                '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
                + ' to learn more about interactive tables.';
              element.innerHTML = '';
              dataTable['output_type'] = 'display_data';
              await google.colab.output.renderOutput(dataTable, element);
              const docLink = document.createElement('div');
              docLink.innerHTML = docLinkHtml;
              element.appendChild(docLink);
            }
          </script>
        </div>
      </div>




We can obtain the description for a particular language as

.. code:: python

    note_df['note'].loc[note_df['lang'] == 'en'].values[0]




.. parsed-literal::

    "World War I (WWI or WW1), also known as the First World War, was a global war centred in Europe that began on 28 July 1914 and lasted until 11 November 1918. From the time of its occurrence until the approach of World War II, it was called simply the World War or the Great War, and thereafter the First World War or World War I. In America, it was initially called the European War. More than 9 million combatants were killed; a casualty rate exacerbated by the belligerents' technological and industrial sophistication, and tactical stalemate. It was one of the deadliest conflicts in history, paving the way for major political changes, including revolutions in many of the nations involved.The war drew in all the world's economic great powers, which were assembled in two opposing alliances: the Allies (based on the Triple Entente of the United Kingdom, France and the Russian Empire) and the Central Powers of Germany and Austria-Hungary. Although Italy had also been a member of the Triple Alliance alongside Germany and Austria-Hungary, it did not join the Central Powers, as Austria-Hungary had taken the offensive against the terms of the alliance. These alliances were both reorganised and expanded as more nations entered the war: Italy, Japan and the United States joined the Allies, and the Ottoman Empire and Bulgaria the Central Powers. Ultimately, more than 70 million military personnel, including 60 million Europeans, were mobilised in one of the largest wars in history.Although a resurgence of imperialism was an underlying cause, the immediate trigger for war was the 28 June 1914 assassination of Archduke Franz Ferdinand of Austria, heir to the throne of Austria-Hungary, by Yugoslav nationalist Gavrilo Princip in Sarajevo. This set off a diplomatic crisis when Austria-Hungary delivered an ultimatum to the Kingdom of Serbia, and international alliances formed over the previous decades were invoked. Within weeks, the major powers were at war and the conflict soon spread around the world.On 28 July, the Austro-Hungarians fired the first shots in preparation for the invasion of Serbia. As Russia mobilised, Germany invaded neutral Belgium and Luxembourg before moving towards France, leading Britain to declare war on Germany. After the German march on Paris was halted, what became known as the Western Front settled into a battle of attrition, with a trench line that would change little until 1917. Meanwhile, on the Eastern Front, the Russian army was successful against the Austro-Hungarians, but was stopped in its invasion of East Prussia by the Germans. In November 1914, the Ottoman Empire joined the war, opening fronts in the Caucasus, Mesopotamia and the Sinai. Italy and Bulgaria went to war in 1915, Romania in 1916, and the United States in 1917.The war approached a resolution after the Russian government collapsed in March, 1917, and a subsequent revolution in November brought the Russians to terms with the Central Powers. On 4 November 1918, the Austro-Hungarian empire agreed to an armistice. After a 1918 German offensive along the western front, the Allies drove back the Germans in a series of successful offensives and began entering the trenches. Germany, which had its own trouble with revolutionaries, agreed to an armistice on 11 November 1918, ending the war in victory for the Allies.By the end of the war, four major imperial powers—the German, Russian, Austro-Hungarian and Ottoman empires—ceased to exist. The successor states of the former two lost substantial territory, while the latter two were dismantled. The map of Europe was redrawn, with several independent nations restored or created. The League of Nations formed with the aim of preventing any repetition of such an appalling conflict. This aim failed, with weakened states, renewed European nationalism and the German feeling of humiliation contributing to the rise of fascism and the conditions for World War II."



Tips for using entities with the Search API
-------------------------------------------

Once we know the identifier for a certain entity we can use the Search
API to obtain objects containing it.

For instance we can query objects containing the entity “Painting” using
its uri http://data.europeana.eu/concept/base/47

.. code:: python

    concept_uri = 'http://data.europeana.eu/concept/base/47'
    resp = apis.search(
        query = f'"{concept_uri}"'
    )
    
    resp['totalResults']




.. parsed-literal::

    120708



Notice that in order to use a uri as a query we need to wrap it in
quotation marks ““.

We might want to query for object belonging to more than one entity. We
can simply do that by using logical operators in the query. Querying for
paintings from the 16th century:

.. code:: python

    resp = apis.search(
        query = '"http://data.europeana.eu/timespan/16" AND "http://data.europeana.eu/concept/base/47"',
        media = True,
        qf = 'TYPE:IMAGE'
    )
    
    resp['totalResults']




.. parsed-literal::

    300



Queyring for paintings with some relation to Paris

.. code:: python

    resp = apis.search(
        query = '"http://data.europeana.eu/place/base/41488" AND "http://data.europeana.eu/concept/base/47"',
        media = True,
        qf = 'TYPE:IMAGE'
    )
    
    resp['totalResults']




.. parsed-literal::

    14



When querying for entities uris, the objects returned are those that
have the requested uris in the metadata.

However, not all objects contain this information and instead many of
them contain the name of the entity. It is always a good idea to query
for the name of the entities as well, as there might be more objects:

.. code:: python

    resp = apis.search(
        query = 'Paris AND Painting',
        media = True,
        qf = 'TYPE:IMAGE'
    )
    
    resp['totalResults']




.. parsed-literal::

    3612



Conclusions
-----------

In this tutorial we learned:

-  What types of entities are available in the Europeana Entity API

-  To use the ``suggest`` method for obtaining entities of a certain
   type matching a text query

-  To use the ``retrieve`` method for obtaining information about an
   individual entity of a certain type

-  To use the method ``resolve`` for obtaining entities that match a
   query url

-  To process some of the fields contained in the responses of the
   methods above and convert the responses to Pandas dataframes

-  To query for entities using Europeana Search API
