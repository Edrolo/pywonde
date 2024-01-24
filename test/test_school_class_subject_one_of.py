# coding: utf-8

"""
    Wonde API

    API Docs

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from wonde.models.school_class_subject_one_of import SchoolClassSubjectOneOf  # noqa: E501

class TestSchoolClassSubjectOneOf(unittest.TestCase):
    """SchoolClassSubjectOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchoolClassSubjectOneOf:
        """Test SchoolClassSubjectOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchoolClassSubjectOneOf`
        """
        model = SchoolClassSubjectOneOf()  # noqa: E501
        if include_optional:
            return SchoolClassSubjectOneOf(
                data = wonde.models.subject.Subject(
                    id = 'A1362597725', 
                    mis_id = '520', 
                    code = 'Bi', 
                    name = 'Biology', 
                    active = True, 
                    created_at = wonde.models.date_time_object.DateTimeObject(
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        timezone_type = 3, 
                        timezone = 'UTC', ), 
                    updated_at = wonde.models.date_time_object.DateTimeObject(
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        timezone_type = 3, 
                        timezone = 'UTC', ), )
            )
        else:
            return SchoolClassSubjectOneOf(
        )
        """

    def testSchoolClassSubjectOneOf(self):
        """Test SchoolClassSubjectOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()