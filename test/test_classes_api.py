"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

import wonde


class TestClassesApi(unittest.TestCase):
    """ClassesApi unit test stubs"""

    def setUp(self):
        self.api = wonde.api.classes_api.ClassesApi()

    def tearDown(self):
        pass

    def test_get_school_class(self):
        """Test case for get_school_class

        Get specific class for a school  # noqa: E501
        """
        pass

    def test_list_school_classes(self):
        """Test case for list_school_classes

        Get all classes for a school  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
