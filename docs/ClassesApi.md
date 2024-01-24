# wonde.ClassesApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_school_class**](ClassesApi.md#get_school_class) | **GET** /schools/{school_id}/classes/{class_id} | Get specific class for a school
[**list_school_classes**](ClassesApi.md#list_school_classes) | **GET** /schools/{school_id}/classes | Get all classes for a school


# **get_school_class**
> GetSchoolClass200Response get_school_class(school_id, class_id, include=include)

Get specific class for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.get_school_class200_response import GetSchoolClass200Response
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
    except Exception as e:
        print("Exception when calling ClassesApi->get_school_class: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **class_id** | **str**| The ID of the class | 
 **include** | [**List[str]**](str.md)| Comma separated list of objects to include | [optional] 

### Return type

[**GetSchoolClass200Response**](GetSchoolClass200Response.md)

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

# **list_school_classes**
> ListSchoolClasses200Response list_school_classes(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, include=include, has_students=has_students, has_lessons=has_lessons, class_name=class_name, class_subject=class_subject)

Get all classes for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_school_classes200_response import ListSchoolClasses200Response
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
    page = 56 # int | Page offset for offset-paginated results. (optional)
    cursor = 'cursor_example' # str | Page cursor for cursor-paginated results. (optional)
    include = 'include_example' # str | Comma separated list of objects to include (optional)
    has_students = True # bool | Only get classes that have students (optional)
    has_lessons = True # bool | Only get classes that have lessons (optional)
    class_name = 'class_name_example' # str | Return results with the provided class name (optional)
    class_subject = 'class_subject_example' # str | Return results with the provided subject id (optional)

    try:
        # Get all classes for a school
        api_response = api_instance.list_school_classes(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, include=include, has_students=has_students, has_lessons=has_lessons, class_name=class_name, class_subject=class_subject)
        print("The response of ClassesApi->list_school_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassesApi->list_school_classes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **page** | **int**| Page offset for offset-paginated results. | [optional] 
 **cursor** | **str**| Page cursor for cursor-paginated results. | [optional] 
 **include** | **str**| Comma separated list of objects to include | [optional] 
 **has_students** | **bool**| Only get classes that have students | [optional] 
 **has_lessons** | **bool**| Only get classes that have lessons | [optional] 
 **class_name** | **str**| Return results with the provided class name | [optional] 
 **class_subject** | **str**| Return results with the provided subject id | [optional] 

### Return type

[**ListSchoolClasses200Response**](ListSchoolClasses200Response.md)

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

