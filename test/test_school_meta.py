"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.school_meta import SchoolMeta


class TestSchoolMeta(unittest.TestCase):
    """SchoolMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchoolMeta:
        """Test SchoolMeta
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SchoolMeta`
        """
        model = SchoolMeta()  # noqa: E501
        if include_optional:
            return SchoolMeta(
                online = True,
                approved = True,
                audited = True,
                custom_attendance_codes = True
            )
        else:
            return SchoolMeta(
        )
        """

    def testSchoolMeta(self):
        """Test SchoolMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
