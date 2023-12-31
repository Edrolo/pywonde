"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest


class TestEmployee(unittest.TestCase):
    """Employee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Employee
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Employee`
        """
        model = wonde.models.employee.Employee()  # noqa: E501
        if include_optional :
            return Employee(
                id = 'A1329183376', 
                upi = '5cc4ab015f8f7870b581e30e0ef474fa', 
                mis_id = '26', 
                title = 'Mrs', 
                initials = 'SS', 
                surname = 'Smith', 
                forename = 'Sally', 
                middle_names = 'Victoria', 
                legal_surname = 'Smith', 
                legal_forename = 'Sally', 
                gender = 'female', 
                date_of_birth = '1963-02-11T00:00Z', 
                restored_at = wonde.models.date_time_object.DateTimeObject(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timezone_type = 3, 
                    timezone = 'UTC', ), 
                created_at = wonde.models.date_time_object.DateTimeObject(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timezone_type = 3, 
                    timezone = 'UTC', ), 
                updated_at = wonde.models.date_time_object.DateTimeObject(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timezone_type = 3, 
                    timezone = 'UTC', )
            )
        else :
            return Employee(
        )
        """

    def testEmployee(self):
        """Test Employee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
