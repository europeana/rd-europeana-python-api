
from PIL import Image
import requests

from io import BytesIO


class Description(dict):

    def __init__(self,desc,**kw):
        super(Description, self).__init__(desc, **kw)
        
        if not isinstance(desc,dict):
            raise ValueError('Europeana API: input must be a dictionary')

        self.update({k:v[0] for k,v in self.items()})
        self.lang = list(self.keys())

    # def __str__(self):
    #     return ''


class Title(dict):

    def __init__(self,title,**kw):
        super(Title, self).__init__(title, **kw)
        
        if not isinstance(title,dict):
            raise ValueError('Europeana API: input must be a dictionary')

        self.update({k:v[0] for k,v in self.items()})
        self.lang = list(self.keys())

    # def __str__(self):
    #     return ''


class EDM:


  def __init__(self,edm_object):
    
    # edm attributes
    self.completeness = None
    self.country = None
    self.dataProvider = None
    self.dcDescriptionLangAware = None
    self.dcLanguage = None
    self.dcTitleLangAware = None
    self.edmDatasetName = None
    self.edmIsShownBy = None
    self.edmIsShownAt = None
    self.edmPreview = None
    self.type = None
    self.id = None
    self.edmPlaceLabelLangAware = None
    self.year = None

    # own attributes
    self.media_url = None
    self.provider_url = None
    self.thumbnail_url = None
    self.rights_url = None

    self.description = None
    self.title = None
    self.place = None
    self.lang = None

    # edm attributes
    if 'completeness' in edm_object:
      self.completeness = edm_object['completeness']

    if 'country' in edm_object:
      self.country = edm_object['country'][0]
    
    if 'dataProvider' in edm_object:
      self.dataProvider = edm_object['dataProvider'][0]
    
    if 'edmDatasetName' in edm_object:
      self.edmDatasetName = edm_object['edmDatasetName']

    if 'year' in edm_object:
      self.year = edm_object['year'][0]

    if 'rights' in edm_object:
      self.rights_url = edm_object['rights'][0]

    if 'id' in edm_object:
      self.id = edm_object['id']

    if 'type' in edm_object:
      self.type = edm_object['type']

    # own attributes
    if 'edmIsShownBy' in edm_object:
      self.edmIsShownBy = edm_object['edmIsShownBy']
      self.media_url = self.edmIsShownBy[0]
    
    if 'edmIsShownAt' in edm_object:
      self.edmIsShownAt = edm_object['edmIsShownAt']
      self.provider_url = self.edmIsShownAt[0]

    if 'edmPreview' in edm_object:
      self.edmPreview = edm_object['edmPreview']
      self.thumbnail_url = self.edmPreview[0]

    if 'dcDescriptionLangAware' in edm_object:
      self.dcDescriptionLangAware = edm_object['dcDescriptionLangAware']
      self.description = Description(self.dcDescriptionLangAware)

    if 'dcTitleLangAware' in edm_object:
      self.dcTitleLangAware = edm_object['dcTitleLangAware']
      self.title = Title(self.dcTitleLangAware)

    if 'edmPlaceLabelLangAware' in edm_object:
      self.edmPlaceLabelLangAware = edm_object['edmPlaceLabelLangAware']
      self.place = Title(self.edmPlaceLabelLangAware)

    if 'dcLanguage' in edm_object:
      self.dcLanguage = edm_object['dcLanguage']
      self.lang = self.dcLanguage





    


    

    
