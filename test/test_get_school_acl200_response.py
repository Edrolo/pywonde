"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.get_school_acl200_response import GetSchoolAcl200Response


class TestGetSchoolAcl200Response(unittest.TestCase):
    """GetSchoolAcl200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSchoolAcl200Response:
        """Test GetSchoolAcl200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetSchoolAcl200Response`
        """
        model = GetSchoolAcl200Response()  # noqa: E501
        if include_optional:
            return GetSchoolAcl200Response(
                data = wonde.models.acl.ACL(
                    mode = '', 
                    ids = [
                        null
                        ], )
            )
        else:
            return GetSchoolAcl200Response(
        )
        """

    def testGetSchoolAcl200Response(self):
        """Test GetSchoolAcl200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
