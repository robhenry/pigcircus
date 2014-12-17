import unittest
from querystrings import test_querystring_helper

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_querystring_helper.querystring_helper_tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
