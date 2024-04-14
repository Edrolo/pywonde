"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import unittest

from wonde.models.deletion import Deletion


class TestDeletion(unittest.TestCase):
    """Deletion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Deletion:
        """Test Deletion
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Deletion`
        """
        model = Deletion()  # noqa: E501
        if include_optional:
            return Deletion(
                type = '',
                id = '',
                mis_id = '',
                deleted_at = wonde.models.date_time_object.DateTimeObject(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timezone_type = 3, 
                    timezone = 'UTC', ),
                restored_at = wonde.models.date_time_object.DateTimeObject(
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timezone_type = 3, 
                    timezone = 'UTC', )
            )
        else:
            return Deletion(
        )
        """

    def testDeletion(self):
        """Test Deletion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
