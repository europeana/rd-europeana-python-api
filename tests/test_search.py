import unittest

from pyeuropeana.apis import SearchWrapper
import pyeuropeana.utils.edm_utils as edm_utils

class TestSearch(unittest.TestCase):

    def test_args(self):
        
        # Test that at least one argument is being passed
       
        with self.assertRaises(ValueError) as context:
            SearchWrapper()
        self.assertTrue('No arguments passed' in str(context.exception))

        
        # Test that the api throws a warning when invalid arguments are passed
        
        with self.assertRaises(ValueError) as context:
            SearchWrapper(
                wskey = 'api2demo',
                queryf = '',
                row = 12
            )
        self.assertTrue("Invalid arguments detected: ['queryf', 'row']" in str(context.exception))


if __name__ == "__main__":
    unittest.main()



    



   
