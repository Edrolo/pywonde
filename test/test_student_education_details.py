"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.student_education_details import StudentEducationDetails


class TestStudentEducationDetails(unittest.TestCase):
    """StudentEducationDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StudentEducationDetails:
        """Test StudentEducationDetails
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `StudentEducationDetails`
        """
        model = StudentEducationDetails()  # noqa: E501
        if include_optional:
            return StudentEducationDetails(
                data = wonde.models.education_details.EducationDetails(
                    current_nc_year = '', 
                    local_upn = '', )
            )
        else:
            return StudentEducationDetails(
        )
        """

    def testStudentEducationDetails(self):
        """Test StudentEducationDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
