"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest


class TestMetaSchoolsSchoolIdPermissionsGet200Response(unittest.TestCase):
    """MetaSchoolsSchoolIdPermissionsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetaSchoolsSchoolIdPermissionsGet200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MetaSchoolsSchoolIdPermissionsGet200Response`
        """
        model = wonde.models.meta_schools_school_id_permissions_get200_response.MetaSchoolsSchoolIdPermissionsGet200Response()  # noqa: E501
        if include_optional :
            return MetaSchoolsSchoolIdPermissionsGet200Response(
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
        else :
            return MetaSchoolsSchoolIdPermissionsGet200Response(
        )
        """

    def testMetaSchoolsSchoolIdPermissionsGet200Response(self):
        """Test MetaSchoolsSchoolIdPermissionsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()