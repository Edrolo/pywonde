# pywonde
API Docs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Edrolo/pywonde.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Edrolo/pywonde.git`)

Then import the package:
```python
import wonde
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wonde
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import wonde
from wonde.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wonde.com/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = wonde.Configuration(
    host = "https://api.wonde.com/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = wonde.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: BearerAuth
configuration = wonde.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with wonde.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wonde.ClassesApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    class_id = 'class_id_example' # str | The ID of the class
    include = ['include_example'] # List[str] | Comma separated list of objects to include (optional)

    try:
        # Get specific class for a school
        api_response = api_instance.get_school_class(school_id, class_id, include=include)
        print("The response of ClassesApi->get_school_class:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClassesApi->get_school_class: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wonde.com/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClassesApi* | [**get_school_class**](docs/ClassesApi.md#get_school_class) | **GET** /schools/{school_id}/classes/{class_id} | Get specific class for a school
*ClassesApi* | [**list_school_classes**](docs/ClassesApi.md#list_school_classes) | **GET** /schools/{school_id}/classes | Get all classes for a school
*DeletionsApi* | [**list_school_deletions**](docs/DeletionsApi.md#list_school_deletions) | **GET** /schools/{school_id}/deletions | Get deletions for a school
*EmployeesApi* | [**get_school_employee**](docs/EmployeesApi.md#get_school_employee) | **GET** /schools/{school_id}/employees/{employee_id} | Get specific employee for a school
*EmployeesApi* | [**list_school_employees**](docs/EmployeesApi.md#list_school_employees) | **GET** /schools/{school_id}/employees | Get all employees for a school
*LessonsApi* | [**get_school_lesson**](docs/LessonsApi.md#get_school_lesson) | **GET** /schools/{school_id}/lessons/{lesson_id} | Returns a specific lesson for a specific school
*LessonsApi* | [**list_school_lessons**](docs/LessonsApi.md#list_school_lessons) | **GET** /schools/{school_id}/lessons | Returns a list of lessons for a specific school
*SchoolsApi* | [**get_school**](docs/SchoolsApi.md#get_school) | **GET** /schools/{school_id} | Retrieve a specific school
*SchoolsApi* | [**get_school_acl**](docs/SchoolsApi.md#get_school_acl) | **GET** /meta/schools/{school_id}/acl | Retrieve the access control list applied to a school
*SchoolsApi* | [**get_school_meta**](docs/SchoolsApi.md#get_school_meta) | **GET** /meta/schools/{school_id} | Retrieve meta data for a school
*SchoolsApi* | [**get_school_permissions**](docs/SchoolsApi.md#get_school_permissions) | **GET** /meta/schools/{school_id}/permissions | Retrieve the permissions applied to a school
*SchoolsApi* | [**list_schools**](docs/SchoolsApi.md#list_schools) | **GET** /schools/all | Retrieve all schools
*SchoolsApi* | [**list_schools_approved**](docs/SchoolsApi.md#list_schools_approved) | **GET** /schools | Retrieve all approved schools
*SchoolsApi* | [**list_schools_audited**](docs/SchoolsApi.md#list_schools_audited) | **GET** /schools/audited | Retrieve all audited schools
*SchoolsApi* | [**list_schools_declined**](docs/SchoolsApi.md#list_schools_declined) | **GET** /schools/declined | Retrieve all schools with declined access
*SchoolsApi* | [**list_schools_offline**](docs/SchoolsApi.md#list_schools_offline) | **GET** /schools/offline | Retrieve all offline schools
*SchoolsApi* | [**list_schools_pending**](docs/SchoolsApi.md#list_schools_pending) | **GET** /schools/pending | Retrieve all schools with pending access request
*SchoolsApi* | [**list_schools_revoked**](docs/SchoolsApi.md#list_schools_revoked) | **GET** /schools/revoked | Retrieve all schools with revoked access
*SchoolsApi* | [**request_school_access**](docs/SchoolsApi.md#request_school_access) | **POST** /schools/{school_id}/request-access | Request access to a school
*SchoolsApi* | [**revoke_school_access**](docs/SchoolsApi.md#revoke_school_access) | **DELETE** /schools/{school_id}/revoke-access | Revoke access to a school
*StudentsApi* | [**get_school_student**](docs/StudentsApi.md#get_school_student) | **GET** /schools/{school_id}/students/{student_id} | Retrieve a specific student in a specific school
*StudentsApi* | [**list_school_students**](docs/StudentsApi.md#list_school_students) | **GET** /schools/{school_id}/students | Retrieve a list of students for a specific school
*SubjectsApi* | [**get_school_subject**](docs/SubjectsApi.md#get_school_subject) | **GET** /schools/{school_id}/subjects/{subject_id} | Retrieve a specific subject for a school
*SubjectsApi* | [**list_school_subjects**](docs/SubjectsApi.md#list_school_subjects) | **GET** /schools/{school_id}/subjects | Retrieve subjects for a school


## Documentation For Models

 - [ACL](docs/ACL.md)
 - [ACLIdsInner](docs/ACLIdsInner.md)
 - [ACLIdsInnerOneOf](docs/ACLIdsInnerOneOf.md)
 - [Contact](docs/Contact.md)
 - [ContactDetails](docs/ContactDetails.md)
 - [ContactDetailsEmails](docs/ContactDetailsEmails.md)
 - [DateTimeObject](docs/DateTimeObject.md)
 - [Deletion](docs/Deletion.md)
 - [EducationDetails](docs/EducationDetails.md)
 - [Employee](docs/Employee.md)
 - [EmployeeContactDetails](docs/EmployeeContactDetails.md)
 - [GetSchool200Response](docs/GetSchool200Response.md)
 - [GetSchoolAcl200Response](docs/GetSchoolAcl200Response.md)
 - [GetSchoolClass200Response](docs/GetSchoolClass200Response.md)
 - [GetSchoolMeta200Response](docs/GetSchoolMeta200Response.md)
 - [GetSchoolPermissions200Response](docs/GetSchoolPermissions200Response.md)
 - [Lesson](docs/Lesson.md)
 - [ListSchoolClasses200Response](docs/ListSchoolClasses200Response.md)
 - [ListSchoolDeletions200Response](docs/ListSchoolDeletions200Response.md)
 - [ListSchoolEmployees200Response](docs/ListSchoolEmployees200Response.md)
 - [ListSchoolLessons200Response](docs/ListSchoolLessons200Response.md)
 - [ListSchoolLessons200ResponseMeta](docs/ListSchoolLessons200ResponseMeta.md)
 - [ListSchoolStudents200Response](docs/ListSchoolStudents200Response.md)
 - [ListSchoolSubjects200Response](docs/ListSchoolSubjects200Response.md)
 - [ListSchools200Response](docs/ListSchools200Response.md)
 - [Meta](docs/Meta.md)
 - [Pagination](docs/Pagination.md)
 - [Permission](docs/Permission.md)
 - [RequestSchoolAccess200Response](docs/RequestSchoolAccess200Response.md)
 - [RequestSchoolAccessRequest](docs/RequestSchoolAccessRequest.md)
 - [School](docs/School.md)
 - [SchoolAddress](docs/SchoolAddress.md)
 - [SchoolAddressAddressCountry](docs/SchoolAddressAddressCountry.md)
 - [SchoolClass](docs/SchoolClass.md)
 - [SchoolClassEmployees](docs/SchoolClassEmployees.md)
 - [SchoolClassLessons](docs/SchoolClassLessons.md)
 - [SchoolClassStudents](docs/SchoolClassStudents.md)
 - [SchoolClassSubject](docs/SchoolClassSubject.md)
 - [SchoolClassSubjectOneOf](docs/SchoolClassSubjectOneOf.md)
 - [SchoolExtended](docs/SchoolExtended.md)
 - [SchoolMeta](docs/SchoolMeta.md)
 - [SchoolRegion](docs/SchoolRegion.md)
 - [SchoolRegionIdentifiers](docs/SchoolRegionIdentifiers.md)
 - [Student](docs/Student.md)
 - [StudentEducationDetails](docs/StudentEducationDetails.md)
 - [Subject](docs/Subject.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication

<a id="BasicAuth"></a>
### BasicAuth

- **Type**: HTTP basic authentication


## Author




