import unittest
import querystring_helper 

class querystring_helper_tests(unittest.TestCase):

    def test_should_return_querystring_param_when_exsits(self):
        self.assertEqual(querystring_helper.parse_querystring_value('message', 'http://www.google.com?message=hello'), 'hello')

    def test_should_return_none_when_querystring_doesnt_exist(self):
        self.assertEqual(querystring_helper.parse_querystring_value('message', 'http://www.google.com'), None)

    def test_should_return_none_when_bad_url(self):
        self.assertEqual(querystring_helper.parse_querystring_value('message', 'notaurl'), None)

    def test_should_return_none_when_url_is_none(self):
        self.assertEqual(querystring_helper.parse_querystring_value('message', None), None)
