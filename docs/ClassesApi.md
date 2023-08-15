# wonde.ClassesApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schools_school_id_classes_class_id_get**](ClassesApi.md#schools_school_id_classes_class_id_get) | **GET** /schools/{school_id}/classes/{class_id} | Get specific class for a school
[**schools_school_id_classes_get**](ClassesApi.md#schools_school_id_classes_get) | **GET** /schools/{school_id}/classes | Get all classes for a school


# **schools_school_id_classes_class_id_get**
> ModelClass schools_school_id_classes_class_id_get(school_id, class_id)

Get specific class for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.model_class import ModelClass
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
    except Exception as e:
        print("Exception when calling ClassesApi->schools_school_id_classes_class_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **class_id** | **str**| The ID of the class | 

### Return type

[**ModelClass**](ModelClass.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A class for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schools_school_id_classes_get**
> SchoolsSchoolIdClassesGet200Response schools_school_id_classes_get(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, has_students=has_students, has_lessons=has_lessons, class_name=class_name, class_subject=class_subject)

Get all classes for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_school_id_classes_get200_response import SchoolsSchoolIdClassesGet200Response
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
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    include = 'include_example' # str | Comma separated list of objects to include (optional)
    has_students = True # bool | Only get classes that have students (optional)
    has_lessons = True # bool | Only get classes that have lessons (optional)
    class_name = 'class_name_example' # str | Return results with the provided class name (optional)
    class_subject = 'class_subject_example' # str | Return results with the provided subject id (optional)

    try:
        # Get all classes for a school
        api_response = api_instance.schools_school_id_classes_get(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, has_students=has_students, has_lessons=has_lessons, class_name=class_name, class_subject=class_subject)
        print("The response of ClassesApi->schools_school_id_classes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassesApi->schools_school_id_classes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **include** | **str**| Comma separated list of objects to include | [optional] 
 **has_students** | **bool**| Only get classes that have students | [optional] 
 **has_lessons** | **bool**| Only get classes that have lessons | [optional] 
 **class_name** | **str**| Return results with the provided class name | [optional] 
 **class_subject** | **str**| Return results with the provided subject id | [optional] 

### Return type

[**SchoolsSchoolIdClassesGet200Response**](SchoolsSchoolIdClassesGet200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of classes for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

