import unittest
import uuid_helper 

class uuid_helper_tests(unittest.TestCase):

    def test_should_return_a_uuid_when_requested(self):
        self.assertEqual(len(uuid_helper.create_uuid()), 36)

    def test_should_return_unique_uuid(self):
        self.assertNotEqual(uuid_helper.create_uuid(), uuid_helper.create_uuid())
