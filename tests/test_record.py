import unittest

from pyeuropeana.apis import RecordAPI
from pyeuropeana.utils.edm_utils import process_CHO_record

# caution: avoid that the exceptions depend on the error messages of the api

class TestRecord(unittest.TestCase):
    def test_api_key(self):
        """
        Test that the api key is correct
        """
        with self.assertRaises(ValueError) as context:
            RecordAPI('wrong_key')
        self.assertTrue("API key doesn't exist" in str(context.exception))

    def test_input_id(self):
        """
        Test valid id
        """
        record_api = RecordAPI('api2demo')
        with self.assertRaises(ValueError) as context:
            record_api(87)
        self.assertTrue("the input should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record_api(0.5)
        self.assertTrue("the input should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record_api(True)
        self.assertTrue("the input should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record_api('asdf')
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record_api('/asdfa345sdf')
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record_api('asdfa/345sdf')
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record_api('/79/resource_document_museumboerhaave')
        self.assertTrue("Invalid record identifier" in str(context.exception))


if __name__ == "__main__":
    unittest.main()



