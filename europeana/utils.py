import os
import urllib
import requests

from PIL import Image
from io import BytesIO

#import numpy as np
#import pprint

from schema import Schema, And, Or, Use, Optional




def url2img(url):
    try:
        response = requests.get(url)
        return Image.open(BytesIO(response.content))
    except:
        print('Europeana API: Failed to get media image')
        pass


def format_where(where):
    try:
        return '(where:{})'.format(Schema(And(str)).validate(where))
    except:
        raise ValueError('EuropeanaAPI: "where" must be a string')


def format_who(who):
    try:
        return '(who:{})'.format(Schema(And(str)).validate(who))
    except:
        raise ValueError('EuropeanaAPI: "who" must be a string')


def format_lat(lat):
    try:
        lat = Schema([Use(float,int),Use(float,int)]).validate(lat)
        return '(pl_wgs84_pos_lat:[{} TO {}])'.format(lat[0],lat[1])
    except:
        raise ValueError('EuropeanaAPI: "lat" must have the form [-30.5,45]')

def format_lon(lon):
    try:
        lon = Schema([Use(float,int),Use(float,int)]).validate(lon)
        return '(pl_wgs84_pos_long:[{} TO {}])'.format(lon[0],lon[1])
    except:
        raise ValueError('EuropeanaAPI: "lon" must have the form [-30.5,45]')

def format_range(rang):
    try:
        rang = Schema([And(str),And(str)]).validate(rang)
        return '([{} TO {}])'.format(rang[0],rang[1])
    except:
        raise ValueError('EuropeanaAPI: "range" must have the form ["a","z"]')


def validate_reusability(reusability):
    try:
        reusability = Schema(And(str)).validate(reusability)
        if reusability not in ['open','restricted','permission']:
          print(f'EuropeanaAPI: WARNING: value "{reusability}" for reusability unknown. Set to all possible options of reusability')
        return reusability
    except:
        raise ValueError(f'EuropeanaAPI: "reusability" must be "open","restricted" or "permission"')


def validate_rows(rows):
    try:
        rows = Schema(And(Use(int), lambda n: 0 <= n)).validate(rows)
        if rows > 100:
          rows = 100
          print(f'EuropeanaAPI: WARNING: value "rows" is > 100. Set to 100.')
        return rows
    except:
        raise ValueError('EuropeanaAPI: "rows" must be a non-negative integer <=  100')


def validate_start(start):
    try:
        start = Schema(And(Use(int), lambda n: 1 <= n <= 100)).validate(start)
        if start > 100:
          start = 100
          print(f'EuropeanaAPI: WARNING: value "start" is > 100. Set to 100.')
        return start
    except:
        raise ValueError('EuropeanaAPI: "start" must be an integer >= 1 and <= 100')


def validate_media(media):
    try:
        return Schema(And(bool)).validate(media)
    except:
        raise ValueError('EuropeanaAPI: "media" must be True or False')


def validate_thumbnail(thumbnail):
    try:
        return Schema(And(bool)).validate(thumbnail)
    except:
        raise ValueError('EuropeanaAPI: "thumbnail" must be True or False')

def validate_landingpage(landingpage):
    try:
        return Schema(And(bool)).validate(landingpage)
    except:
        raise ValueError('EuropeanaAPI: "landingpage" must be True or False')

def validate_logic(logic):
    try:
        return Schema(And(Use(str), lambda n: n in ['AND','OR'])).validate(logic)
    except:
        raise ValueError('EuropeanaAPI: "logic" must be "AND" or "OR"')


def validate_n(n):
    try:
        return Schema(And(Use(int), lambda x: 1 <= x <= 10000)).validate(n)
    except:
        raise ValueError('EuropeanaAPI: n must be a positive integer smaller than 10000')


def validate_sort(sort):
  sort_list = ['score', 'timestamp_created', 'timestamp_update', 'europeana_id', 'COMPLETENESS', 'is_fulltext', 'has_thumbnails', 'has_media']

  schema = Schema(Or(
      {'term': lambda n: n in sort_list, Optional('order', default='asc'): lambda n: n in ['asc','desc']},
      And(Use(str),lambda n: n in sort_list)
  ))

  try:
    validated = schema.validate(sort)
    if isinstance(validated,str):
      return '{}+asc'.format(validated)
    else:
      return '{}+{}'.format(validated['term'],validated['order']) 

  except:
    raise ValueError('Europeana API: sort must be a string term_value or a dict \
    {"term":term_value,"order":order_value} where term_value in \
     ["score", "timestamp_created", "timestamp_update", "europeana_id", "COMPLETENESS", "is_fulltext", "has_thumbnails, "has_media"] \
     and order_value in ["asc","desc"]')





