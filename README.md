# pywonde
API Docs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

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

    try:
        # Get specific class for a school
        api_response = api_instance.schools_school_id_classes_class_id_get(school_id, class_id)
        print("The response of ClassesApi->schools_school_id_classes_class_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClassesApi->schools_school_id_classes_class_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wonde.com/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClassesApi* | [**schools_school_id_classes_class_id_get**](docs/ClassesApi.md#schools_school_id_classes_class_id_get) | **GET** /schools/{school_id}/classes/{class_id} | Get specific class for a school
*ClassesApi* | [**schools_school_id_classes_get**](docs/ClassesApi.md#schools_school_id_classes_get) | **GET** /schools/{school_id}/classes | Get all classes for a school
*DeletionsApi* | [**schools_school_id_deletions_get**](docs/DeletionsApi.md#schools_school_id_deletions_get) | **GET** /schools/{school_id}/deletions | Get deletions for a school
*EmployeesApi* | [**schools_school_id_employees_employee_id_get**](docs/EmployeesApi.md#schools_school_id_employees_employee_id_get) | **GET** /schools/{school_id}/employees/{employee_id} | Get specific employee for a school
*EmployeesApi* | [**schools_school_id_employees_get**](docs/EmployeesApi.md#schools_school_id_employees_get) | **GET** /schools/{school_id}/employees | Get all employees for a school
*LessonsApi* | [**get_school_lesson_by_id**](docs/LessonsApi.md#get_school_lesson_by_id) | **GET** /schools/{school_id}/lessons/{lesson_id} | Returns a specific lesson for a specific school
*LessonsApi* | [**get_school_lessons**](docs/LessonsApi.md#get_school_lessons) | **GET** /schools/{school_id}/lessons | Returns a list of lessons for a specific school
*SchoolsApi* | [**get_school**](docs/SchoolsApi.md#get_school) | **GET** /schools/{school_id} | Retrieve a specific school
*SchoolsApi* | [**meta_schools_school_id_acl_get**](docs/SchoolsApi.md#meta_schools_school_id_acl_get) | **GET** /meta/schools/{school_id}/acl | Retrieve the access control list applied to a school
*SchoolsApi* | [**meta_schools_school_id_get**](docs/SchoolsApi.md#meta_schools_school_id_get) | **GET** /meta/schools/{school_id} | Retrieve meta data for a school
*SchoolsApi* | [**meta_schools_school_id_permissions_get**](docs/SchoolsApi.md#meta_schools_school_id_permissions_get) | **GET** /meta/schools/{school_id}/permissions | Retrieve the permissions applied to a school
*SchoolsApi* | [**schools_all_get**](docs/SchoolsApi.md#schools_all_get) | **GET** /schools/all | Retrieve all schools
*SchoolsApi* | [**schools_approved_get**](docs/SchoolsApi.md#schools_approved_get) | **GET** /schools/approved | Retrieve all approved schools
*SchoolsApi* | [**schools_audited_get**](docs/SchoolsApi.md#schools_audited_get) | **GET** /schools/audited | Retrieve all audited schools
*SchoolsApi* | [**schools_declined_get**](docs/SchoolsApi.md#schools_declined_get) | **GET** /schools/declined | Retrieve all schools with declined access
*SchoolsApi* | [**schools_offline_get**](docs/SchoolsApi.md#schools_offline_get) | **GET** /schools/offline | Retrieve all offline schools
*SchoolsApi* | [**schools_pending_get**](docs/SchoolsApi.md#schools_pending_get) | **GET** /schools/pending | Retrieve all schools with pending access request
*SchoolsApi* | [**schools_revoked_get**](docs/SchoolsApi.md#schools_revoked_get) | **GET** /schools/revoked | Retrieve all schools with revoked access
*SchoolsApi* | [**schools_school_id_request_access_post**](docs/SchoolsApi.md#schools_school_id_request_access_post) | **POST** /schools/{school_id}/request-access | Request access to a school
*SchoolsApi* | [**schools_school_id_revoke_access_delete**](docs/SchoolsApi.md#schools_school_id_revoke_access_delete) | **DELETE** /schools/{school_id}/revoke-access | Revoke access to a school
*StudentsApi* | [**get_student**](docs/StudentsApi.md#get_student) | **GET** /schools/{school_id}/students/{student_id} | Retrieve a specific student in a specific school
*StudentsApi* | [**list_students**](docs/StudentsApi.md#list_students) | **GET** /schools/{school_id}/students | Retrieve a list of students for a specific school
*SubjectsApi* | [**get_subject**](docs/SubjectsApi.md#get_subject) | **GET** /schools/{school_id}/subjects/{subject_id} | Retrieve a specific subject for a school
*SubjectsApi* | [**get_subjects**](docs/SubjectsApi.md#get_subjects) | **GET** /schools/{school_id}/subjects | Retrieve subjects for a school


## Documentation For Models

 - [ACL](docs/ACL.md)
 - [ACLIdsInner](docs/ACLIdsInner.md)
 - [Contact](docs/Contact.md)
 - [DateTimeObject](docs/DateTimeObject.md)
 - [Deletion](docs/Deletion.md)
 - [Employee](docs/Employee.md)
 - [GetSchoolLessons200Response](docs/GetSchoolLessons200Response.md)
 - [GetSchoolLessons200ResponseMeta](docs/GetSchoolLessons200ResponseMeta.md)
 - [GetSubjects200Response](docs/GetSubjects200Response.md)
 - [Lesson](docs/Lesson.md)
 - [ListStudents200Response](docs/ListStudents200Response.md)
 - [Meta](docs/Meta.md)
 - [MetaSchoolsSchoolIdAclGet200Response](docs/MetaSchoolsSchoolIdAclGet200Response.md)
 - [MetaSchoolsSchoolIdGet200Response](docs/MetaSchoolsSchoolIdGet200Response.md)
 - [MetaSchoolsSchoolIdPermissionsGet200Response](docs/MetaSchoolsSchoolIdPermissionsGet200Response.md)
 - [ModelClass](docs/ModelClass.md)
 - [Pagination](docs/Pagination.md)
 - [Permission](docs/Permission.md)
 - [School](docs/School.md)
 - [SchoolAddress](docs/SchoolAddress.md)
 - [SchoolAddressAddressCountry](docs/SchoolAddressAddressCountry.md)
 - [SchoolExtended](docs/SchoolExtended.md)
 - [SchoolMeta](docs/SchoolMeta.md)
 - [SchoolRegion](docs/SchoolRegion.md)
 - [SchoolRegionIdentifiers](docs/SchoolRegionIdentifiers.md)
 - [SchoolsAllGet200Response](docs/SchoolsAllGet200Response.md)
 - [SchoolsSchoolIdClassesGet200Response](docs/SchoolsSchoolIdClassesGet200Response.md)
 - [SchoolsSchoolIdDeletionsGet200Response](docs/SchoolsSchoolIdDeletionsGet200Response.md)
 - [SchoolsSchoolIdEmployeesGet200Response](docs/SchoolsSchoolIdEmployeesGet200Response.md)
 - [SchoolsSchoolIdRequestAccessPost200Response](docs/SchoolsSchoolIdRequestAccessPost200Response.md)
 - [SchoolsSchoolIdRequestAccessPostRequest](docs/SchoolsSchoolIdRequestAccessPostRequest.md)
 - [Student](docs/Student.md)
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



