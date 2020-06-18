from .edm import EDM



class SearchResponse:
    """
    Documentation of the search response here

    Attributes :
        query : str
        success : bool

        params : dict, Search parameters
        api_response : dict, Original Search API response
        
        num_items : int, Number of items returned by the response
        edm_items : list, Items modeled with the Europeana Data Model
        totalResults : int, Total number of items that match with the query 

    """
    def __init__(self,response, query, **kwargs):

        # query attributes
        self.query = query
        self.params = kwargs

        # response attributes
        self.api_response = response
        self.success = response['success']

        print('in search response {}'.format(response['success']))

        self.num_items = None
        self.edm_items = None
        self.totalResults = None

        if self.success:
            self.items = response['items']
            self.num_items = len(self.items)
            self.edm_items = [EDM(item) for item in self.items]
            self.totalResults = response['totalResults']


        
            


        
        






        