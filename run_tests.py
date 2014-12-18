import unittest
from querystring import test_querystring_helper
from guid import test_uuid_helper
from url import test_url_helper
from coalesce import test_coalesce_helper

if __name__ == '__main__':
    querystring_suite = unittest.TestLoader().loadTestsFromTestCase(test_querystring_helper.querystring_helper_tests)
    url_suite = unittest.TestLoader().loadTestsFromTestCase(test_url_helper.url_helper_tests)
    uuid_suite = unittest.TestLoader().loadTestsFromTestCase(test_uuid_helper.uuid_helper_tests)
    coalesce_suite = unittest.TestLoader().loadTestsFromTestCase(test_coalesce_helper.coalesce_helper_tests)

    alltests = unittest.TestSuite([url_suite, uuid_suite, coalesce_suite])
    unittest.TextTestRunner(verbosity=2).run(alltests)
