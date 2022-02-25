import unittest

from pyeuropeana.apis import search

class TestSearch(unittest.TestCase):

    def test_args(self):
        
        # Test that at least one argument is being passed
       
        with self.assertRaises(ValueError) as context:
            search()
        self.assertTrue('No arguments passed' in str(context.exception))

        


if __name__ == "__main__":
    #unittest.main()

    



    



   
