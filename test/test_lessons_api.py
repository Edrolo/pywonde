"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

import wonde


class TestLessonsApi(unittest.TestCase):
    """LessonsApi unit test stubs"""

    def setUp(self):
        self.api = wonde.api.lessons_api.LessonsApi()

    def tearDown(self):
        pass

    def test_get_school_lesson(self):
        """Test case for get_school_lesson

        Returns a specific lesson for a specific school  # noqa: E501
        """
        pass

    def test_list_school_lessons(self):
        """Test case for list_school_lessons

        Returns a list of lessons for a specific school  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
