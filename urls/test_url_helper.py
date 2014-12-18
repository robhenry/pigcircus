import unittest
import url_helper 

class url_helper_tests(unittest.TestCase):

    def test_should_return_scheme_when_given_valid_url(self):
        self.assertEqual(url_helper.parse_url_part('scheme', 'http://www.google.com?x=1'), 'http')

    def test_should_return_path_when_given_valid_url(self):
        self.assertEqual(url_helper.parse_url_part('path', 'http://www.google.com/search?x=1'), '/search')

    def test_should_return_query_when_given_valid_url(self):
        self.assertEqual(url_helper.parse_url_part('query', 'http://www.google.com/search?x=1'), 'x=1')

    def test_should_return_netloc_when_given_valid_url(self):
        self.assertEqual(url_helper.parse_url_part('netloc', 'http://www.google.com/search?x=1'), 'www.google.com')

    def test_should_return_none_when_given_bad_url(self):
        self.assertEqual(url_helper.parse_url_part('netloc', 'www.google.com/search?x=1'), None)

    def test_should_return_none_when_given_none(self):
        self.assertEqual(url_helper.parse_url_part('netloc', None), None)

