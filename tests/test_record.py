import unittest

from pyeuropeana.apis import RecordWrapper
from pyeuropeana.utils.edm_utils import process_CHO_record

# caution: avoid that the exceptions depend on the error messages of the api

class TestRecord(unittest.TestCase):

    def test_input_id(self):
        """
        Test valid id
        """
        with self.assertRaises(ValueError) as context:
            RecordWrapper(
                record_id = 2,
                )
        self.assertTrue("the input id should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
          RecordWrapper(
                record_id = True,
                )
        self.assertTrue("the input id should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
          RecordWrapper(
                record_id = 'asfd',
                )
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            RecordWrapper(
                    record_id = '/asdfa345sdf',
                    )
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            RecordWrapper(
                        record_id = 'asdfa/345sdf',
                        )
        self.assertTrue("Not valid Europeana id" in str(context.exception))


if __name__ == "__main__":
    unittest.main()



