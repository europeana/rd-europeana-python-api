import requests
from ..utils.auth import get_api_key

def suggest(**kwargs):
  """
  Suggest method of the Entity API [1]. Returns entities based on a text query

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.entity.suggest(
  >>>    text = 'leonardo',
  >>>    TYPE = 'agent',
  >>>    language = 'de',
  >>>     )
  
  Args:
      text (:obj:`str`)
        The search term(s)
      TYPE (:obj:`str`, optional)
         Used to restrict search for a specific entity type (agents, places, concepts and time spans), otherwise all.
      language (:obj:`str`, optional)
         The language (two or three letters ISO639 language code) in which the text is written. If omitted, defaults to English ("en").
                              
  Returns: :obj:`dict`
    The suggest method returns a list of 10 suggest entities. For some entities (in particular people/agents) it returns some contextual
    information is known such as the profession, date of birth and date of death. For other entities it just returns the label (prefLabel) 
    in the given language, the entity type and the entity identifier. For a full list of data fields, please see the Entity context definition.

  References: 
    1. https://pro.europeana.eu/page/entity
 
  """
  wskey = get_api_key()
  language = kwargs.get('language','en')
  TYPE = kwargs.get('TYPE')
  text = kwargs.get('text')
  if not kwargs:
    raise ValueError('No arguments passed')
  if not text:
    raise ValueError('Argument "text" is needed')
  return requests.get(f'https://api.europeana.eu/entity/suggest',params = {'wskey':wskey,'text':text,'type':TYPE,'language':language}).json()


def retrieve(**kwargs):
  """
  Retrieve method of the Entity API [1]. Returns information about a particular entity

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.entity.retrieve(
  >>>    TYPE = 'agent',
  >>>    IDENTIFIER = 3,
  >>>     )
  
  Args:
    TYPE (:obj:`str`)
        The type of the entity, either: "agent", "concept", "place" or "timespan".
    IDENTIFIER (:obj:`int`)
        The local identifier for the entity.

  Returns: :obj:`dict`
    The retrieve method returns all known information about an entity in all languages in which the information is available.
    This includes all localised labels (prefLabel), contextual information such as biography and all references of the same entity
    in other external data sources (sameAs). For a full list of data fields, please see the Entity context definition.

  References:
    1. https://pro.europeana.eu/page/entity
 
  """
  wskey = get_api_key()
  TYPE = kwargs.get('TYPE')
  IDENTIFIER = kwargs.get('IDENTIFIER')
  if not kwargs:
    raise ValueError('No arguments passed')
  return requests.get(f'https://api.europeana.eu/entity/{TYPE}/base/{IDENTIFIER}.json',params = {'wskey':wskey}).json()

def resolve(uri):
  """
  Resolve method of the Entity API [1]. Searches for an entity given an input URI

  >>> import pyeuropeana.apis as apis
  >>> resp = apis.entity.resolve('http://dbpedia.org/resource/Leonardo_da_Vinci')

  Args:
    uri (:obj:`str`)
        The external identifier (as an URI) for the entity.

  Returns: :obj:`dict`
    On success, the method returns a HTTP 301 with the Europeana URI within the Location Header field.

  References:
    1. https://pro.europeana.eu/page/entity
 
  """
  wskey = get_api_key()
  if not isinstance(uri,str):
    raise ValueError('input uri must be a string')
  response = requests.get(f'https://api.europeana.eu/entity/resolve/',params = {'wskey':wskey,'uri':uri}).json()
  if 'success' in  response.keys():
    raise ValueError(response['error'])
  return response
   

