import unittest
from pyeuropeana.apis import EntityAPI

class TestEntity(unittest.TestCase):

    # note: there seems to be no authentication in place, so a test for the api key is not needed

    def test_suggest(self):
        """
        Test that at least one argument is being passed
        """
        entity_api = EntityAPI('api2demo')
        with self.assertRaises(ValueError) as context:
            entity_api.suggest()
        self.assertTrue('No arguments passed' in str(context.exception))

        with self.assertRaises(ValueError) as context:
        entity_api.suggest(
            TYPE = 'agent',
        )
        self.assertTrue('Argument "text" is needed' in str(context.exception))

    def test_retrieve(self):
        """
        Test that at least one argument is being passed
        """
        entity_api = EntityAPI('api2demo')
        with self.assertRaises(ValueError) as context:
            entity_api.retrieve()
        self.assertTrue('No arguments passed' in str(context.exception))

        # to do: add more tests for retrieve
        

    def test_resolve(self):
        with self.assertRaises(ValueError) as context:
            entity_api = EntityAPI('api2demo')
            entity_api.resolve(2)
        self.assertTrue('input uri must be a string' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            entity_api.resolve('http://dbpedia.org/resource/Leonardo_da_Vinc')
        self.assertTrue('No entity found for' in str(context.exception)) # caution, test depending on output of entity api


if __name__ == '__main__':
    unittest.main()


