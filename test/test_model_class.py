"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest


class TestModelClass(unittest.TestCase):
    """ModelClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ModelClass`
        """
        model = wonde.models.model_class.ModelClass()  # noqa: E501
        if include_optional :
            return ModelClass(
                id = 'A1329183376', 
                mis_id = '8925', 
                name = '10A/Ar1', 
                code = '10A/Ar1', 
                description = '10A/Ar1', 
                subject = 'Mathematics', 
                alternative = False, 
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
            return ModelClass(
        )
        """

    def testModelClass(self):
        """Test ModelClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()