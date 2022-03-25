import unittest

from pyeuropeana.apis import record


class TestRecord(unittest.TestCase):
    def test_input_id(self):
        """
        Test valid id
        """
        with self.assertRaises(ValueError) as context:
            record(2)
        self.assertTrue("the input id should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record(True)
        self.assertTrue("the input id should be a string" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record("asfd")
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record("/asdfa345sdf")
        self.assertTrue("Not valid Europeana id" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            record("asdfa/345sdf")
        self.assertTrue("Not valid Europeana id" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
