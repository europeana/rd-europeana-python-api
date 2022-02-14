import unittest
from pyeuropeana.apis import EntityAPI

# to do: test suggest
# TYPE: str, categories?
# text: str


# to do: test retrieve

# to do: check for incorrect arguments

class TestEntity(unittest.TestCase):

    # Caution: it seems there is no authentication in the Entity api, so this test should be avoided 

    # def test_api_key(self):
    #     """
    #     Test that the api key is correct
    #     """
    #     with self.assertRaises(ValueError) as context:
    #         EntityAPI('wrong_key')
    #     self.assertTrue("API key doesn't exist" in str(context.exception))

    def test_suggest_no_args(self):
        """
        Test that at least one argument is being passed
        """
        with self.assertRaises(ValueError) as context:
            entity_api = EntityAPI('api2demo')
            entity_api.suggest()
        self.assertTrue('No arguments passed' in str(context.exception))

    def test_retrieve_no_args(self):
        """
        Test that at least one argument is being passed
        """
        with self.assertRaises(ValueError) as context:
            entity_api = EntityAPI('api2demo')
            entity_api.retrieve()
        self.assertTrue('No arguments passed' in str(context.exception))



if __name__ == '__main__':
    #unittest.main()

    entity_api = EntityAPI('wrong_key')

    resp = entity_api.suggest(
        TYPE = 'agen',
        text = 'leonardo'
    )

    print(resp)

    # resp = entity_api.retrieve(
    #     TYPE = 'agent',
    #     IDENTIFIER = 25980
    # )

    # print(resp)

