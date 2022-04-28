import unittest
import pytest

import pyeuropeana.apis as apis


@pytest.mark.skip(reason="needs further work/data mocks because of API calls")
class TestEntity(unittest.TestCase):
    def test_suggest(self):
        """
        Test that at least one argument is being passed
        """
        with self.assertRaises(ValueError) as context:
            apis.entity.suggest()
        self.assertTrue("No arguments passed" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            apis.entity.suggest(
                TYPE="agent",
            )
        self.assertTrue('Argument "text" is needed' in str(context.exception))

    def test_retrieve(self):
        """
        Test that at least one argument is being passed
        """
        with self.assertRaises(ValueError) as context:
            apis.entity.retrieve()
        self.assertTrue("No arguments passed" in str(context.exception))

    def test_resolve(self):
        with self.assertRaises(ValueError) as context:
            apis.entity.resolve(2)
        self.assertTrue("input uri must be a string" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
