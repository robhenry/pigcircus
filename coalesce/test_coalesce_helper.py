import unittest
import coalesce_helper 

class coalesce_helper_tests(unittest.TestCase):

    def test_should_return_first_value(self):
        self.assertEqual(coalesce_helper.coalesce(None, 'test2', None, 'test'), 'test2')

    def test_should_return_none_if_no_value(self):
        self.assertEqual(coalesce_helper.coalesce(None, None, None), None)
