"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest


class TestSchoolAddressAddressCountry(unittest.TestCase):
    """SchoolAddressAddressCountry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SchoolAddressAddressCountry
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SchoolAddressAddressCountry`
        """
        model = wonde.models.school_address_address_country.SchoolAddressAddressCountry()  # noqa: E501
        if include_optional :
            return SchoolAddressAddressCountry(
                code = 'GBR', 
                name = 'United Kingdom'
            )
        else :
            return SchoolAddressAddressCountry(
        )
        """

    def testSchoolAddressAddressCountry(self):
        """Test SchoolAddressAddressCountry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()