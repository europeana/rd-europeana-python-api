
.. note:: **You can download this tutorial in the .ipynb format or the .py format.**

  :download:`Download Python source code <tutorial_translation_files/tutorial_translation.py>`

  :download:`Download as Jupyter Notebook <tutorial_translation_files/tutorial_translation.ipynb>`

Translation Tutorial
===================


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
    os.environ['EUROPEANA_API_KEY'] = 'api2demo'

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

    response




.. parsed-literal::

    {'apikey': 'api2demo',
     'success': True,
     'requestNumber': 999,
     'itemsCount': 10,
     'totalResults': 615941,
     'nextCursor': 'AoE/DS85MjAwMjI3L0JpYmxpb2dyYXBoaWNSZXNvdXJjZV8zMDAwMDczOTc0MDc0',
     'items': [{'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcDescription': ['Manifesto che riporta due carte geografiche dell\'Europa, nella prima si evidenziano i territori occupati dagli Alleati, nella seconda si mostra la superficie del "Territorio degli Alleati che è stato occupato temporaneamente dagli Imperi Centrali"'],
       'dcDescriptionLangAware': {'it': ['Manifesto che riporta due carte geografiche dell\'Europa, nella prima si evidenziano i territori occupati dagli Alleati, nella seconda si mostra la superficie del "Territorio degli Alleati che è stato occupato temporaneamente dagli Imperi Centrali"']},
       'dcTitleLangAware': {'it': ["L'insegnamento della carta geografica della guerra"]},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358106_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358106_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358106_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755040_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755040_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755040_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541682343,
       'timestamp_created': '2014-04-02T08:58:20.400Z',
       'timestamp_created_epoch': 1396429100400,
       'timestamp_update': '2014-07-09T14:26:52.277Z',
       'timestamp_update_epoch': 1404916012277,
       'title': ["L'insegnamento della carta geografica della guerra"],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcCreator': ['Croce Rossa Americana'],
       'dcCreatorLangAware': {'def': ['Croce Rossa Americana']},
       'dcDescription': ["Manifesto che mostra al centro la carta geografica dell'Italia in cui sono indicati i luoghi dove la Croce rossa americana è presente sul territorio,  intorno fanno da cornice alcune fotografie che documentano il lavoro svolto dalla Croce rossa americana, in alto sono presenti i ritratti fotografici di Woodrow Wilson, Robert Perkins ed Henry P. Davison."],
       'dcDescriptionLangAware': {'it': ["Manifesto che mostra al centro la carta geografica dell'Italia in cui sono indicati i luoghi dove la Croce rossa americana è presente sul territorio,  intorno fanno da cornice alcune fotografie che documentano il lavoro svolto dalla Croce rossa americana, in alto sono presenti i ritratti fotografici di Woodrow Wilson, Robert Perkins ed Henry P. Davison."]},
       'dcTitleLangAware': {'it': ['Croce rossa americana']},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0195860_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0195860_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0195860_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755038_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755038_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755038_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541682087,
       'timestamp_created': '2014-04-02T08:58:20.398Z',
       'timestamp_created_epoch': 1396429100398,
       'timestamp_update': '2014-07-09T14:26:52.218Z',
       'timestamp_update_epoch': 1404916012218,
       'title': ['Croce rossa americana'],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcDescription': ["Manifesto che mostra una carta geografica dell'Italia nord-orientale e, in un riquadro in basso a sinistra, le immagini  dei rappresentanti delle nazioni alleate, ritratti a mezzo busto"],
       'dcDescriptionLangAware': {'it': ["Manifesto che mostra una carta geografica dell'Italia nord-orientale e, in un riquadro in basso a sinistra, le immagini  dei rappresentanti delle nazioni alleate, ritratti a mezzo busto"]},
       'dcTitleLangAware': {'it': ['Carta della guerra italo-austriaca  : gli alleati contro i barbari']},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358097_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358097_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358097_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755037_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755037_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755037_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681929,
       'timestamp_created': '2014-04-02T08:58:20.374Z',
       'timestamp_created_epoch': 1396429100374,
       'timestamp_update': '2014-07-09T14:26:52.213Z',
       'timestamp_update_epoch': 1404916012213,
       'title': ['Carta della guerra italo-austriaca  : gli alleati contro i barbari'],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcDescription': ["Manifesto che mostra al centro una carta geografica del mondo in cui sono indicate  l'area approssimativa del territorio occupato dagli Imperi Centrali  e l'area approssimativa del territorio occupato dagli alleati al 2 agosto 1916, intorno, in sei riquadri, sono fornite informazioni sull'Esercito Inglese e sulla Marina  Britannica"],
       'dcDescriptionLangAware': {'it': ["Manifesto che mostra al centro una carta geografica del mondo in cui sono indicate  l'area approssimativa del territorio occupato dagli Imperi Centrali  e l'area approssimativa del territorio occupato dagli alleati al 2 agosto 1916, intorno, in sei riquadri, sono fornite informazioni sull'Esercito Inglese e sulla Marina  Britannica"]},
       'dcTitleLangAware': {'it': ["L'impero britannico in guerra  : gli uomini dell'impero  : le loro case ed i loro campi di battaglia"]},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/PIS0009069_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/PIS0009069_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FPIS0009069_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755035_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755035_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755035_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681653,
       'timestamp_created': '2014-04-02T08:58:20.318Z',
       'timestamp_created_epoch': 1396429100318,
       'timestamp_update': '2014-07-09T14:26:52.180Z',
       'timestamp_update_epoch': 1404916012180,
       'title': ["L'impero britannico in guerra  : gli uomini dell'impero  : le loro case ed i loro campi di battaglia"],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcCreator': ['Ferrovie dello stato: Servizio commerciale'],
       'dcCreatorLangAware': {'def': ['Ferrovie dello stato: Servizio commerciale']},
       'dcDescription': ['Manifesto che mostra una carta geografica dell\'Italia nord-orientale e una della Dalmazia e riporta una legenda con la "spiegazione delle linee" ed un "elenco delle ferrovie locali"'],
       'dcDescriptionLangAware': {'it': ['Manifesto che mostra una carta geografica dell\'Italia nord-orientale e una della Dalmazia e riporta una legenda con la "spiegazione delle linee" ed un "elenco delle ferrovie locali"']},
       'dcTitleLangAware': {'it': ["Linee ferroviarie comprese nella zona di territorio fra l'attuale confino politico nord-orientale e quello geografico  / compilata dal servizio commerciale delle Ferrovie dello Stato"]},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358010_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358010_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358010_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755033_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755033_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755033_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681467,
       'timestamp_created': '2014-04-02T08:58:20.374Z',
       'timestamp_created_epoch': 1396429100374,
       'timestamp_update': '2014-07-09T14:26:52.194Z',
       'timestamp_update_epoch': 1404916012194,
       'title': ["Linee ferroviarie comprese nella zona di territorio fra l'attuale confino politico nord-orientale e quello geografico  / compilata dal servizio commerciale delle Ferrovie dello Stato"],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcDescription': ["Manifesto che mostra una carta geografica dell'Italia e dei Balcani in cui sono indicati, in vari colori, gli eserciti mobilizzati dai vari paesi coinvolti nella prima guerra mondiale"],
       'dcDescriptionLangAware': {'it': ["Manifesto che mostra una carta geografica dell'Italia e dei Balcani in cui sono indicati, in vari colori, gli eserciti mobilizzati dai vari paesi coinvolti nella prima guerra mondiale"]},
       'dcTitleLangAware': {'it': ["Guerra europea (Guerra d'Italia e dei Balcani), armate europee di terra e di mare"]},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358105_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358105_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358105_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755031_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755031_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755031_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681364,
       'timestamp_created': '2014-04-02T08:58:20.370Z',
       'timestamp_created_epoch': 1396429100370,
       'timestamp_update': '2014-07-09T14:26:52.100Z',
       'timestamp_update_epoch': 1404916012100,
       'title': ["Guerra europea (Guerra d'Italia e dei Balcani), armate europee di terra e di mare"],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcDescription': ['Manifesto che mostra la carta geografica del mondo su cui sono indicate in rosso le terre su cui la Germania ha delle mire e riporta, in un riquadro in alto a destra, trentasei citazioni in cui vengono giustificate tali pretese territoriali'],
       'dcDescriptionLangAware': {'it': ['Manifesto che mostra la carta geografica del mondo su cui sono indicate in rosso le terre su cui la Germania ha delle mire e riporta, in un riquadro in alto a destra, trentasei citazioni in cui vengono giustificate tali pretese territoriali']},
       'dcTitleLangAware': {'it': ["Ce que l'Allemagne désire, ses aspirations telles qu'elles sont exprimées par les principaux penseurs allemands"]},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358053_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358053_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358053_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755030_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755030_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755030_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681311,
       'timestamp_created': '2014-04-02T08:58:20.351Z',
       'timestamp_created_epoch': 1396429100351,
       'timestamp_update': '2014-07-09T14:26:52.098Z',
       'timestamp_update_epoch': 1404916012098,
       'title': ["Ce que l'Allemagne désire, ses aspirations telles qu'elles sont exprimées par les principaux penseurs allemands"],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 9,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcCreator': ['Frigè, Domenico'],
       'dcCreatorLangAware': {'def': ['Frigè, Domenico']},
       'dcDescription': ["Manifesto che mostra una rappresentazione geografica dell'Europa all'interno di una cornice tipografica decorativa"],
       'dcDescriptionLangAware': {'it': ["Manifesto che mostra una rappresentazione geografica dell'Europa all'interno di una cornice tipografica decorativa"]},
       'dcTitleLangAware': {'it': ['Europa panoramica (fronte unico), febbraio 1917  / D. Frige']},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358041_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358041_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358041_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 9,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755029_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755029_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755029_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681254,
       'timestamp_created': '2014-04-02T08:58:20.369Z',
       'timestamp_created_epoch': 1396429100369,
       'timestamp_update': '2014-07-09T14:26:52.110Z',
       'timestamp_update_epoch': 1404916012110,
       'title': ['Europa panoramica (fronte unico), febbraio 1917  / D. Frige'],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcDescription': ["Manifesto che raffigura in azzurro la catena dei monti e il corso dei fiumi del Trentino Alto Adige, dell'Istria e della Dalmazia"],
       'dcDescriptionLangAware': {'it': ["Manifesto che raffigura in azzurro la catena dei monti e il corso dei fiumi del Trentino Alto Adige, dell'Istria e della Dalmazia"]},
       'dcTitleLangAware': {'it': ["L'Italia agli italiani!  : Trento e il Trentino, Trieste e l'Istria, Fiume e la Dalmazia sono dunque italiane anche per ragioni geografiche"]},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/IEI0366844_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/IEI0366844_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FIEI0366844_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755028_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755028_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755028_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541681166,
       'timestamp_created': '2014-04-02T08:58:20.268Z',
       'timestamp_created_epoch': 1396429100268,
       'timestamp_update': '2014-07-09T14:26:52.094Z',
       'timestamp_update_epoch': 1404916012094,
       'title': ["L'Italia agli italiani!  : Trento e il Trentino, Trieste e l'Istria, Fiume e la Dalmazia sono dunque italiane anche per ragioni geografiche"],
       'type': 'IMAGE',
       'ugc': [False]},
      {'completeness': 10,
       'country': ['Italy'],
       'dataProvider': ['Central Institute for the Union Catalogue of Italian Libraries'],
       'dcCreator': ['Comitato nazionale tra il personale delle ferrovie dello Stato per gli indumenti di lana ai soldati'],
       'dcCreatorLangAware': {'def': ['Comitato nazionale tra il personale delle ferrovie dello Stato per gli indumenti di lana ai soldati']},
       'dcDescription': ["Manifesto che mostra la carta geograficha della Venezia Tridentina, della Venezia Giulia e della Dalmazia, sulla sinistra la bandiera del Regno d'Italia e l'immagine di un leone alato incatenato"],
       'dcDescriptionLangAware': {'it': ["Manifesto che mostra la carta geograficha della Venezia Tridentina, della Venezia Giulia e della Dalmazia, sulla sinistra la bandiera del Regno d'Italia e l'immagine di un leone alato incatenato"]},
       'dcTitleLangAware': {'it': ['Carta delle nostre terre irredente  / Comitato nazionale tra il personale delle Ferrovie dello Stato per gli indumenti di lana pei soldati, Roma']},
       'edmConcept': ['http://data.europeana.eu/concept/loc/sh85148236',
        'http://data.europeana.eu/concept/base/83',
        'http://data.europeana.eu/concept/base/43'],
       'edmConceptLabel': [{'def': 'Erster Weltkrieg, 1914-1918'},
        {'def': 'Erster Weltkrieg'},
        {'def': 'Karte (Kartografie)'},
        {'def': 'World War, 1914-1918'},
        {'def': 'World War I'},
        {'def': 'Map'},
        {'def': 'Guerra mondiale 1914-1918'},
        {'def': 'Prima guerra mondiale'},
        {'def': 'Mappa'},
        {'def': 'Guerre mondiale, 1914-1918'},
        {'def': 'Première Guerre mondiale'},
        {'def': 'Carte géographique'},
        {'def': '1. Verdenskrig, 1914-1918'},
        {'def': '1. verdenskrig'},
        {'def': 'Kort (geografi)'},
        {'def': 'Wereldoorlog, 1914-1918'},
        {'def': 'Prvi svetski rat, 1914-1918'},
        {'def': 'Први светски рат'},
        {'def': 'Карта (мапа)'},
        {'def': 'प्रथम विश्वयुद्ध'},
        {'def': 'मानचित्र'},
        {'def': 'Første verdenskrig'},
        {'def': 'Kart'},
        {'def': 'Первая мировая война'},
        {'def': 'Географическая карта'},
        {'def': 'Першая сусветная вайна'},
        {'def': 'Геаграфічная карта'},
        {'def': 'Ensimmäinen maailmansota'},
        {'def': 'Kartta'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Първа световна война'},
        {'def': 'Карта'},
        {'def': 'Pirmasis pasaulinis karas'},
        {'def': 'Žemėlapis'},
        {'def': 'Pirmais pasaules karš'},
        {'def': 'Ģeogrāfiskā karte'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Zemljovid'},
        {'def': 'Első világháború'},
        {'def': 'Térkép'},
        {'def': 'ערשטע וועלט מלחמה'},
        {'def': 'מאפע'},
        {'def': 'Առաջին համաշխարհային պատերազմ'},
        {'def': 'Քարտեզ'},
        {'def': 'Prvi svjetski rat'},
        {'def': 'Karta'},
        {'def': 'Перша світова війна'},
        {'def': 'Географічна карта'},
        {'def': 'პირველი მსოფლიო ომი'},
        {'def': 'გეოგრაფიული რუკა'},
        {'def': 'Prvá svetová vojna'},
        {'def': 'Mapa'},
        {'def': 'Prva svetovna vojna'},
        {'def': 'Zemljevid'},
        {'def': 'An Chéad Chogadh Domhanda'},
        {'def': 'Léarscáil'},
        {'def': 'An Cogadh Mòr'},
        {'def': 'Lufta e Parë Botërore'},
        {'def': 'Harta'},
        {'def': 'Прва светска војна'},
        {'def': 'Географска карта'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Första världskriget'},
        {'def': 'Karta'},
        {'def': '제1차 세계 대전'},
        {'def': '지도'},
        {'def': 'Primeira Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': 'Α΄ Παγκόσμιος Πόλεμος'},
        {'def': 'Χάρτης'},
        {'def': 'Fyrri heimsstyrjöldin'},
        {'def': 'Landakort'},
        {'def': 'Primera Guerra Mundial'},
        {'def': 'Mapa'},
        {'def': '第一次世界大战'},
        {'def': '地图'},
        {'def': 'Esimene maailmasõda'},
        {'def': 'Kaart'},
        {'def': 'První světová válka'},
        {'def': 'Mapa'},
        {'def': 'Lehen Mundu Gerra'},
        {'def': 'Mapa'},
        {'def': 'الحرب العالمية الأولى'},
        {'def': 'خريطة'},
        {'def': 'Y Rhyfel Byd Cyntaf'},
        {'def': 'Map'},
        {'def': '第一次世界大戦'},
        {'def': '地図'},
        {'def': 'Birinci dünya müharibəsi'},
        {'def': 'Coğrafi xəritə'},
        {'def': 'I wojna światowa'},
        {'def': 'Mapa'},
        {'def': 'מלחמת העולם הראשונה'},
        {'def': 'מפה'},
        {'def': 'Primul Război Mondial'},
        {'def': 'Hartă'},
        {'def': 'I. Dünya Savaşı'},
        {'def': 'Harita'}],
       'edmConceptPrefLabelLangAware': {'de': ['Karte (Kartografie)',
         'Erster Weltkrieg, 1914-1918',
         'Erster Weltkrieg'],
        'hi': ['मानचित्र', 'प्रथम विश्वयुद्ध'],
        'no': ['Første verdenskrig', 'Kart'],
        'ru': ['Первая мировая война', 'Географическая карта'],
        'be': ['Першая сусветная вайна', 'Геаграфічная карта'],
        'fi': ['Kartta', 'Ensimmäinen maailmansota'],
        'pt': ['Primeira Guerra Mundial', 'Mapa'],
        'bg': ['Първа световна война', 'Карта'],
        'lt': ['Pirmasis pasaulinis karas', 'Žemėlapis'],
        'lv': ['Ģeogrāfiskā karte', 'Pirmais pasaules karš'],
        'hr': ['Zemljovid', 'Prvi svjetski rat'],
        'fr': ['Première Guerre mondiale',
         'Guerre mondiale, 1914-1918',
         'Carte géographique'],
        'hu': ['Térkép', 'Első világháború'],
        'yi': ['מאפע', 'ערשטע וועלט מלחמה'],
        'hy': ['Առաջին համաշխարհային պատերազմ', 'Քարտեզ'],
        'bs': ['Prvi svjetski rat', 'Karta'],
        'uk': ['Перша світова війна', 'Географічна карта'],
        'ka': ['პირველი მსოფლიო ომი', 'გეოგრაფიული რუკა'],
        'sk': ['Prvá svetová vojna', 'Mapa'],
        'sl': ['Zemljevid', 'Prva svetovna vojna'],
        'ga': ['Léarscáil', 'An Chéad Chogadh Domhanda'],
        'gd': ['An Cogadh Mòr'],
        'sq': ['Harta', 'Lufta e Parë Botërore'],
        'mk': ['Географска карта', 'Прва светска војна'],
        'ca': ['Mapa', 'Primera Guerra Mundial'],
        'sr': ['Карта (мапа)', 'Prvi svetski rat, 1914-1918', 'Први светски рат'],
        'sv': ['Första världskriget', 'Karta'],
        'ko': ['제1차 세계 대전', '지도'],
        'gl': ['Primeira Guerra Mundial', 'Mapa'],
        'el': ['Χάρτης', 'Α΄ Παγκόσμιος Πόλεμος'],
        'en': ['World War, 1914-1918', 'World War I', 'Map'],
        'is': ['Landakort', 'Fyrri heimsstyrjöldin'],
        'it': ['Prima guerra mondiale', 'Mappa', 'Guerra mondiale 1914-1918'],
        'es': ['Mapa', 'Primera Guerra Mundial'],
        'zh': ['地图', '第一次世界大战'],
        'et': ['Esimene maailmasõda', 'Kaart'],
        'cs': ['Mapa', 'První světová válka'],
        'eu': ['Lehen Mundu Gerra', 'Mapa'],
        'ar': ['خريطة', 'الحرب العالمية الأولى'],
        'cy': ['Y Rhyfel Byd Cyntaf', 'Map'],
        'ja': ['第一次世界大戦', '地図'],
        'az': ['Birinci dünya müharibəsi', 'Coğrafi xəritə'],
        'pl': ['I wojna światowa', 'Mapa'],
        'da': ['Kort (geografi)', '1. Verdenskrig, 1914-1918', '1. verdenskrig'],
        'he': ['מלחמת העולם הראשונה', 'מפה'],
        'ro': ['Hartă', 'Primul Război Mondial'],
        'nl': ['Wereldoorlog, 1914-1918'],
        'tr': ['Harita', 'I. Dünya Savaşı']},
       'edmDatasetName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'edmIsShownAt': ['http://www.14-18.it/mappa/RML0358094_01'],
       'edmIsShownBy': ['http://www.14-18.it/img/mappa/RML0358094_01/full'],
       'edmPreview': ['https://api.europeana.eu/thumbnail/v2/url.json?uri=http%3A%2F%2Fwww.14-18.it%2Fimg%2Fmappa%2FRML0358094_01%2Ffull&type=IMAGE'],
       'europeanaCollectionName': ['9200314_Ag_EU_TEL_a1192b_Collections_1914-1918'],
       'europeanaCompleteness': 10,
       'guid': 'https://www.europeana.eu/item/9200314/BibliographicResource_3000093755025_source?utm_source=api&utm_medium=api&utm_campaign=api2demo',
       'id': '/9200314/BibliographicResource_3000093755025_source',
       'index': 0,
       'language': ['it'],
       'link': 'https://api.europeana.eu/record/9200314/BibliographicResource_3000093755025_source.json?wskey=api2demo',
       'previewNoDistribute': False,
       'provider': ['The European Library'],
       'rights': ['http://rightsstatements.org/vocab/InC/1.0/'],
       'score': 1.0,
       'timestamp': 1635541680852,
       'timestamp_created': '2014-04-02T08:58:20.293Z',
       'timestamp_created_epoch': 1396429100293,
       'timestamp_update': '2014-07-09T14:26:52.027Z',
       'timestamp_update_epoch': 1404916012027,
       'title': ['Carta delle nostre terre irredente  / Comitato nazionale tra il personale delle Ferrovie dello Stato per gli indumenti di lana pei soldati, Roma'],
       'type': 'IMAGE',
       'ugc': [False]}],
     'url': 'https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=proxy_dc_description.it%3A%2A&sort=europeana_id&rows=10&cursor=%2A',
     'params': {'wskey': 'api2demo',
      'query': 'proxy_dc_description.it:*',
      'qf': None,
      'reusability': None,
      'media': None,
      'thumbnail': None,
      'landingpage': None,
      'colourpalette': None,
      'theme': None,
      'sort': 'europeana_id',
      'profile': None,
      'rows': 10,
      'cursor': '*',
      'callback': None,
      'facet': None}}



The response is a rich and complex JSON file, which is essentially a
list of nested dictionaries. The JSON format holds many different
metadata fields, for example ``itemCount`` and ``totalResults``. In many
cases we are not interested in all the metadata fields, but in a subset,
depending on the problem at hand.

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
    df_search.head(2) #visualizing 2 of 10 requested results in tabular form




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
          <th>europeana_id</th>
          <th>uri</th>
          <th>type</th>
          <th>image_url</th>
          <th>country</th>
          <th>description</th>
          <th>title</th>
          <th>creator</th>
          <th>language</th>
          <th>rights</th>
          <th>provider</th>
          <th>dataset_name</th>
          <th>concept</th>
          <th>concept_lang</th>
          <th>description_lang</th>
          <th>title_lang</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>/9200314/BibliographicResource_3000093755040_s...</td>
          <td>http://data.europeana.eu/item/9200314/Bibliogr...</td>
          <td>IMAGE</td>
          <td>http://www.14-18.it/img/mappa/RML0358106_01/full</td>
          <td>Italy</td>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>L'insegnamento della carta geografica della gu...</td>
          <td>None</td>
          <td>it</td>
          <td>http://rightsstatements.org/vocab/InC/1.0/</td>
          <td>Central Institute for the Union Catalogue of I...</td>
          <td>9200314_Ag_EU_TEL_a1192b_Collections_1914-1918</td>
          <td>http://data.europeana.eu/concept/loc/sh85148236</td>
          <td>{'de': 'Karte (Kartografie)', 'hi': 'मानचित्र'...</td>
          <td>{'it': 'Manifesto che riporta due carte geogra...</td>
          <td>{'it': 'L'insegnamento della carta geografica ...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>/9200314/BibliographicResource_3000093755038_s...</td>
          <td>http://data.europeana.eu/item/9200314/Bibliogr...</td>
          <td>IMAGE</td>
          <td>http://www.14-18.it/img/mappa/RML0195860_01/full</td>
          <td>Italy</td>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Croce rossa americana</td>
          <td>Croce Rossa Americana</td>
          <td>it</td>
          <td>http://rightsstatements.org/vocab/InC/1.0/</td>
          <td>Central Institute for the Union Catalogue of I...</td>
          <td>9200314_Ag_EU_TEL_a1192b_Collections_1914-1918</td>
          <td>http://data.europeana.eu/concept/loc/sh85148236</td>
          <td>{'de': 'Karte (Kartografie)', 'hi': 'मानचित्र'...</td>
          <td>{'it': 'Manifesto che mostra al centro la cart...</td>
          <td>{'it': 'Croce rossa americana'}</td>
        </tr>
      </tbody>
    </table>
    </div>



Comparing the headings of the table above with the original JSON file we
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
    df_search.head(2) #visualize the first two rows of the result




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
          <th>europeana_id</th>
          <th>uri</th>
          <th>type</th>
          <th>image_url</th>
          <th>country</th>
          <th>description</th>
          <th>title</th>
          <th>creator</th>
          <th>language</th>
          <th>rights</th>
          <th>provider</th>
          <th>dataset_name</th>
          <th>concept</th>
          <th>concept_lang</th>
          <th>description_lang</th>
          <th>title_lang</th>
          <th>description_en</th>
          <th>description_en_it</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>/9200314/BibliographicResource_3000093755040_s...</td>
          <td>http://data.europeana.eu/item/9200314/Bibliogr...</td>
          <td>IMAGE</td>
          <td>http://www.14-18.it/img/mappa/RML0358106_01/full</td>
          <td>Italy</td>
          <td>Manifesto che riporta due carte geografiche de...</td>
          <td>L'insegnamento della carta geografica della gu...</td>
          <td>None</td>
          <td>it</td>
          <td>http://rightsstatements.org/vocab/InC/1.0/</td>
          <td>Central Institute for the Union Catalogue of I...</td>
          <td>9200314_Ag_EU_TEL_a1192b_Collections_1914-1918</td>
          <td>http://data.europeana.eu/concept/loc/sh85148236</td>
          <td>{'de': 'Karte (Kartografie)', 'hi': 'मानचित्र'...</td>
          <td>{'it': 'Manifesto che riporta due carte geogra...</td>
          <td>{'it': 'L'insegnamento della carta geografica ...</td>
          <td>Poster showing two geographical maps of Europe...</td>
          <td>Manifesto raffigurante due carte geografiche d...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>/9200314/BibliographicResource_3000093755038_s...</td>
          <td>http://data.europeana.eu/item/9200314/Bibliogr...</td>
          <td>IMAGE</td>
          <td>http://www.14-18.it/img/mappa/RML0195860_01/full</td>
          <td>Italy</td>
          <td>Manifesto che mostra al centro la carta geogra...</td>
          <td>Croce rossa americana</td>
          <td>Croce Rossa Americana</td>
          <td>it</td>
          <td>http://rightsstatements.org/vocab/InC/1.0/</td>
          <td>Central Institute for the Union Catalogue of I...</td>
          <td>9200314_Ag_EU_TEL_a1192b_Collections_1914-1918</td>
          <td>http://data.europeana.eu/concept/loc/sh85148236</td>
          <td>{'de': 'Karte (Kartografie)', 'hi': 'मानचित्र'...</td>
          <td>{'it': 'Manifesto che mostra al centro la cart...</td>
          <td>{'it': 'Croce rossa americana'}</td>
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
          <td>0.343750</td>
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
          <td>0.343750</td>
          <td>0.492977</td>
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
          <td>-0.889361</td>
        </tr>
        <tr>
          <th>BLEU_score</th>
          <td>-0.889361</td>
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

