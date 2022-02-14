import unittest

from pyeuropeana.apis import SearchAPI
import pyeuropeana.utils.edm_utils as edm_utils

class TestSearch(unittest.TestCase):
    def test_api_key(self):
        """
        Test that the api key is correct
        """
        with self.assertRaises(ValueError) as context:
            SearchAPI('wrong_key')
        self.assertTrue("API key doesn't exist" in str(context.exception))

    def test_no_args(self):
        """
        Test that at least one argument is being passed
        """
        with self.assertRaises(ValueError) as context:
            search_api = SearchAPI('api2demo')
            search_api()
        self.assertTrue('No arguments passed' in str(context.exception))

    def test_wrong_arguments(self):
        """
        Test that the api throws a warning when invalid arguments are passed
        """
        with self.assertRaises(ValueError) as context:
            search_api = SearchAPI('api2demo')
            search_api(
                queryf = '',
                row = 12
            )
        self.assertTrue("Invalid arguments detected: ['queryf', 'row']" in str(context.exception))

if __name__ == "__main__":
    unittest.main()

    # search_api = SearchAPI('api2demo')
    # r = search_api(
    #     #reusability = 2,
    #     rows = 'a'
    # )
    # print(r['totalResults'])

    # to do: throw a warning when reusability is not in ['open','permission','restricted']
    # to do: enforce media, thumnail and landing page as boolean
    # to do: enforce rows to be a number
    # to do: enforce other variables to be strings
    # to do: test for facets
    # to do: test utils


    



   
