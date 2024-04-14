"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.list_schools200_response import ListSchools200Response


class TestListSchools200Response(unittest.TestCase):
    """ListSchools200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSchools200Response:
        """Test ListSchools200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListSchools200Response`
        """
        model = ListSchools200Response()  # noqa: E501
        if include_optional:
            return ListSchools200Response(
                data = [
                    wonde.models.school.School(
                        id = '', 
                        name = '', 
                        establishment_number = '', 
                        urn = 56, 
                        phase_of_education = '', 
                        la_code = '', 
                        timezone = '', 
                        mis = '', 
                        address = wonde.models.school_address.School_address(
                            address_line_1 = 'St James's Passage', 
                            address_line_2 = 'Duke's Place', 
                            address_town = 'London', 
                            address_postcode = 'EC3A 5DE', 
                            address_country = wonde.models.school_address_address_country.School_address_address_country(
                                code = 'GBR', 
                                name = 'United Kingdom', ), ), 
                        extended = wonde.models.school_extended.School_extended(
                            allows_writeback = True, 
                            has_timetables = True, 
                            has_lesson_attendance = True, ), 
                        region = wonde.models.school_region.School_region(
                            code = 'GBR', 
                            domain = 'api.wonde.com', 
                            school_url = 'https://api.wonde.com/v1.0/schools/A1300691890', 
                            identifiers = wonde.models.school_region_identifiers.School_region_identifiers(
                                la_code = '201', 
                                establishment_number = '3614', 
                                urn = 10000, ), ), )
                    ],
                meta = wonde.models.meta.Meta(
                    pagination = wonde.models.pagination.Pagination(
                        next = 'https://api.wonde.com/v1.0/schools/{school_id}/students/?page=2', 
                        previous = '', 
                        more = True, 
                        per_page = 2, 
                        current_page = 1, ), 
                    includes = [
                        ''
                        ], )
            )
        else:
            return ListSchools200Response(
        )
        """

    def testListSchools200Response(self):
        """Test ListSchools200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
