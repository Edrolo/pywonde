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
                subject = None, 
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
                    timezone = 'UTC', ), 
                students = wonde.models.class_students.Class_students(
                    data = [
                        wonde.models.student.Student(
                            id = 'A1749191433', 
                            upi = '8d444684b7aa79bc97f8594a4aab7ce3', 
                            mis_id = '9919', 
                            initials = 'TS', 
                            surname = 'Smith', 
                            forename = 'Tom', 
                            middle_names = '', 
                            legal_surname = 'Smith', 
                            legal_forename = 'Tom', 
                            gender = 'MALE', 
                            date_of_birth = wonde.models.date_time_object.DateTimeObject(
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                timezone_type = 3, 
                                timezone = 'UTC', ), 
                            restored_at = wonde.models.date_time_object.DateTimeObject(
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                timezone_type = 3, 
                                timezone = 'UTC', ), 
                            created_at = , 
                            updated_at = , )
                        ], ), 
                employees = wonde.models.list_school_employees_200_response.listSchoolEmployees_200_response(
                    data = [
                        wonde.models.employee.Employee(
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
                            updated_at = , )
                        ], ), 
                lessons = wonde.models.class_lessons.Class_lessons(
                    data = [
                        wonde.models.lesson.Lesson(
                            id = '', 
                            room = '', 
                            period = '', 
                            employee_id = '', 
                            period_instance_id = 56, 
                            alternative = True, 
                            start_at = wonde.models.date_time_object.DateTimeObject(
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                timezone_type = 3, 
                                timezone = 'UTC', ), 
                            end_at = wonde.models.date_time_object.DateTimeObject(
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                timezone_type = 3, 
                                timezone = 'UTC', ), 
                            created_at = , 
                            updated_at = , )
                        ], )
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
