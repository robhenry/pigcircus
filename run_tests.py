import unittest
from querystrings import test_querystring_helper
from uuids import test_uuid_helper
from urls import test_url_helper

if __name__ == '__main__':
    querystring_suite = unittest.TestLoader().loadTestsFromTestCase(test_querystring_helper.querystring_helper_tests)
    url_suite = unittest.TestLoader().loadTestsFromTestCase(test_url_helper.url_helper_tests)
    uuid_suite = unittest.TestLoader().loadTestsFromTestCase(test_uuid_helper.uuid_helper_tests)
    unittest.TextTestRunner(verbosity=2).run(querystring_suite)
    unittest.TextTestRunner(verbosity=2).run(url_suite)
    unittest.TextTestRunner(verbosity=2).run(uuid_suite)
