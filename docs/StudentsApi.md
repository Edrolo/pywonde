# wonde.StudentsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_student**](StudentsApi.md#get_student) | **GET** /schools/{school_id}/students/{student_id} | Retrieve a specific student in a specific school
[**list_students**](StudentsApi.md#list_students) | **GET** /schools/{school_id}/students | Retrieve a list of students for a specific school


# **get_student**
> Student get_student(school_id, student_id)

Retrieve a specific student in a specific school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.student import Student
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
    api_instance = wonde.StudentsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school to retrieve the student from
    student_id = 'student_id_example' # str | The ID of the student to retrieve

    try:
        # Retrieve a specific student in a specific school
        api_response = api_instance.get_student(school_id, student_id)
        print("The response of StudentsApi->get_student:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentsApi->get_student: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school to retrieve the student from | 
 **student_id** | **str**| The ID of the student to retrieve | 

### Return type

[**Student**](Student.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A student |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_students**
> ListStudents200Response list_students(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, aspect_id=aspect_id, user_defined_field=user_defined_field, only_user_defined_fields=only_user_defined_fields, only_upns=only_upns, only_mis_ids=only_mis_ids)

Retrieve a list of students for a specific school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_students200_response import ListStudents200Response
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
    api_instance = wonde.StudentsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school.
    updated_after = '2013-10-20' # date | Return rows modified after date. (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date. (optional)
    per_page = 56 # int | Amount of rows to return. (optional)
    include = 'include_example' # str | Comma separated list of objects to include. (optional)
    aspect_id = 'aspect_id_example' # str | If including results, restrict to those for this aspect ID only. (optional)
    user_defined_field = 'user_defined_field_example' # str | Filter students by user defined field key. (optional)
    only_user_defined_fields = 'only_user_defined_fields_example' # str | Filter user defined fields by comma separated list. (optional)
    only_upns = 'only_upns_example' # str | Filter UPNs by comma separated list. (optional)
    only_mis_ids = 'only_mis_ids_example' # str | Filter MIS ids by comma separated list. (optional)

    try:
        # Retrieve a list of students for a specific school
        api_response = api_instance.list_students(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, aspect_id=aspect_id, user_defined_field=user_defined_field, only_user_defined_fields=only_user_defined_fields, only_upns=only_upns, only_mis_ids=only_mis_ids)
        print("The response of StudentsApi->list_students:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentsApi->list_students: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school. | 
 **updated_after** | **date**| Return rows modified after date. | [optional] 
 **updated_before** | **date**| Return rows modified before date. | [optional] 
 **per_page** | **int**| Amount of rows to return. | [optional] 
 **include** | **str**| Comma separated list of objects to include. | [optional] 
 **aspect_id** | **str**| If including results, restrict to those for this aspect ID only. | [optional] 
 **user_defined_field** | **str**| Filter students by user defined field key. | [optional] 
 **only_user_defined_fields** | **str**| Filter user defined fields by comma separated list. | [optional] 
 **only_upns** | **str**| Filter UPNs by comma separated list. | [optional] 
 **only_mis_ids** | **str**| Filter MIS ids by comma separated list. | [optional] 

### Return type

[**ListStudents200Response**](ListStudents200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of students |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

