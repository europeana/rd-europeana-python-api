import unittest
import pytest

from pyeuropeana.apis import search


@pytest.mark.skip(reason="needs further work/data mocks because of API calls")
class TestSearch(unittest.TestCase):
    def test_args(self):

        # Test that at least one argument is being passed

        with self.assertRaises(ValueError) as context:
            search()
        self.assertTrue("No arguments passed" in str(context.exception))


if __name__ == "__main__":
    # unittest.main()
    pass
