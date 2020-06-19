from europeana.api import EuropeanaAPI
from europeana.edm import *
from europeana.utils import url2img


def main():

  eu = EuropeanaAPI('your_API_key')


  
  


  r = eu.search('Amsterdam', n = 500,sort = {'term':'score','order':'asc'},  theme = 'nature')
  print(r.success)

  if r.success:

    for i,edm in enumerate(r.edm_items):

      if edm.title:
        print(edm.title.lang)

  # if edm.description:
  #   print(edm.description.lang)

  # if edm.place:
  #   print(edm.place.lang)

  # if edm.media_url:
  #   img = url2img(edm.media_url)
  #   print(img.size)
  #   # img.save('{}.png'.format(i))

  # if edm.thumbnail_url:
  #   img = url2img(edm.thumbnail_url)
  #   print(img.size)
  #   # img.save('{}.png'.format(i))

  # if edm.rights_url:
  #   print(edm.rights_url)

  # if edm.year:
  #   print(edm.year)

  # if edm.lang:
  #   print(edm.lang)
  #   print(len(edm.lang))

 





  # print(r.api_response.keys())
  # print(r.api_response['error'])

  #print(r.keys())

  #print(r['n'])
  #print(len(r['items']))
  #print(r['totalResults'])


  # print('total number of results: {}'.format(r.totalResults))
  # print('parameters: {}'.format(r.params))
  # print('number of EDM objects: {}'.format(r.num_items))

  # for edm in r.edm_items[:10]:
  #   print(edm.thumbnail_url)
  #   # print(edm.id)
  #   # record_response = eu.record(edm.id)

  # countries = {}
  # for edm in r.edm_items:
  #   if edm.country not in countries.keys():
  #     countries.update({edm.country:1})
  #   else:
  #     countries[edm.country] += 1


  # years = {}
  # for edm in r.edm_items:
  #   if edm.year not in years.keys():
  #     years.update({edm.year:1})
  #   else:
  #     years[edm.year] += 1

  # print(countries)
  # print(years)

      
  #img_id = '/2064107/Museu_ProvidedCHO_Museum_of_English_Rural_Life__University_of_Reading_4966'
  #record_response = eu.record(img_id)
