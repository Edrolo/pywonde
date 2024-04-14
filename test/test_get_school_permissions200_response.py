"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.get_school_permissions200_response import (
    GetSchoolPermissions200Response,
)


class TestGetSchoolPermissions200Response(unittest.TestCase):
    """GetSchoolPermissions200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSchoolPermissions200Response:
        """Test GetSchoolPermissions200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetSchoolPermissions200Response`
        """
        model = GetSchoolPermissions200Response()  # noqa: E501
        if include_optional:
            return GetSchoolPermissions200Response(
                data = [
                    wonde.models.permission.Permission(
                        identity = '', 
                        name = '', 
                        description = '', 
                        parent = '', 
                        group = '', 
                        active_from = wonde.models.date_time_object.DateTimeObject(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            timezone_type = 3, 
                            timezone = 'UTC', ), 
                        optional = True, 
                        approved = True, 
                        audited = True, )
                    ]
            )
        else:
            return GetSchoolPermissions200Response(
        )
        """

    def testGetSchoolPermissions200Response(self):
        """Test GetSchoolPermissions200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
