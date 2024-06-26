"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.list_school_lessons200_response_meta import (
    ListSchoolLessons200ResponseMeta,
)


class TestListSchoolLessons200ResponseMeta(unittest.TestCase):
    """ListSchoolLessons200ResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSchoolLessons200ResponseMeta:
        """Test ListSchoolLessons200ResponseMeta
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListSchoolLessons200ResponseMeta`
        """
        model = ListSchoolLessons200ResponseMeta()  # noqa: E501
        if include_optional:
            return ListSchoolLessons200ResponseMeta(
                pagination = wonde.models.pagination.Pagination(
                    next = 'https://api.wonde.com/v1.0/schools/{school_id}/students/?page=2', 
                    previous = '', 
                    more = True, 
                    per_page = 2, 
                    current_page = 1, ),
                includes = [
                    'class'
                    ]
            )
        else:
            return ListSchoolLessons200ResponseMeta(
        )
        """

    def testListSchoolLessons200ResponseMeta(self):
        """Test ListSchoolLessons200ResponseMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
