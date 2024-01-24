# wonde.LessonsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_school_lesson**](LessonsApi.md#get_school_lesson) | **GET** /schools/{school_id}/lessons/{lesson_id} | Returns a specific lesson for a specific school
[**list_school_lessons**](LessonsApi.md#list_school_lessons) | **GET** /schools/{school_id}/lessons | Returns a list of lessons for a specific school


# **get_school_lesson**
> Lesson get_school_lesson(school_id, lesson_id)

Returns a specific lesson for a specific school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.lesson import Lesson
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
    api_instance = wonde.LessonsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school.
    lesson_id = 'lesson_id_example' # str | The ID of the lesson.

    try:
        # Returns a specific lesson for a specific school
        api_response = api_instance.get_school_lesson(school_id, lesson_id)
        print("The response of LessonsApi->get_school_lesson:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LessonsApi->get_school_lesson: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school. | 
 **lesson_id** | **str**| The ID of the lesson. | 

### Return type

[**Lesson**](Lesson.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_school_lessons**
> ListSchoolLessons200Response list_school_lessons(school_id, updated_after=updated_after, updated_before=updated_before, lessons_start_after=lessons_start_after, lessons_start_before=lessons_start_before, per_page=per_page, include=include)

Returns a list of lessons for a specific school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_school_lessons200_response import ListSchoolLessons200Response
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
    api_instance = wonde.LessonsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school.
    updated_after = '2013-10-20' # date | Return rows modified after date. (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date. (optional)
    lessons_start_after = '2013-10-20' # date | Return rows starting after date. (optional)
    lessons_start_before = '2013-10-20' # date | Return rows starting before date. (optional)
    per_page = 56 # int | Amount of rows to return. (optional)
    include = 'include_example' # str | Comma separated list of objects to include. (optional)

    try:
        # Returns a list of lessons for a specific school
        api_response = api_instance.list_school_lessons(school_id, updated_after=updated_after, updated_before=updated_before, lessons_start_after=lessons_start_after, lessons_start_before=lessons_start_before, per_page=per_page, include=include)
        print("The response of LessonsApi->list_school_lessons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LessonsApi->list_school_lessons: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school. | 
 **updated_after** | **date**| Return rows modified after date. | [optional] 
 **updated_before** | **date**| Return rows modified before date. | [optional] 
 **lessons_start_after** | **date**| Return rows starting after date. | [optional] 
 **lessons_start_before** | **date**| Return rows starting before date. | [optional] 
 **per_page** | **int**| Amount of rows to return. | [optional] 
 **include** | **str**| Comma separated list of objects to include. | [optional] 

### Return type

[**ListSchoolLessons200Response**](ListSchoolLessons200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

