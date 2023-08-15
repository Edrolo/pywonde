# wonde.SubjectsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subject**](SubjectsApi.md#get_subject) | **GET** /schools/{school_id}/subjects/{subject_id} | Retrieve a specific subject for a school
[**get_subjects**](SubjectsApi.md#get_subjects) | **GET** /schools/{school_id}/subjects | Retrieve subjects for a school


# **get_subject**
> Subject get_subject(school_id, subject_id, include=include)

Retrieve a specific subject for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.subject import Subject
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
    api_instance = wonde.SubjectsApi(api_client)
    school_id = 'school_id_example' # str | ID of the school to retrieve the subject from
    subject_id = 'subject_id_example' # str | ID of the subject to retrieve
    include = 'include_example' # str | Comma separated list of objects to include. (optional)

    try:
        # Retrieve a specific subject for a school
        api_response = api_instance.get_subject(school_id, subject_id, include=include)
        print("The response of SubjectsApi->get_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->get_subject: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| ID of the school to retrieve the subject from | 
 **subject_id** | **str**| ID of the subject to retrieve | 
 **include** | **str**| Comma separated list of objects to include. | [optional] 

### Return type

[**Subject**](Subject.md)

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

# **get_subjects**
> GetSubjects200Response get_subjects(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, subject_code=subject_code, subject_name=subject_name)

Retrieve subjects for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.get_subjects200_response import GetSubjects200Response
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
    api_instance = wonde.SubjectsApi(api_client)
    school_id = 'school_id_example' # str | ID of the school to retrieve subjects for
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    include = 'include_example' # str | Comma separated list of objects to include. (optional)
    subject_code = 'subject_code_example' # str | Return results with the provided subject code. (optional)
    subject_name = 'subject_name_example' # str | Return results with the provided subject name. (optional)

    try:
        # Retrieve subjects for a school
        api_response = api_instance.get_subjects(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, subject_code=subject_code, subject_name=subject_name)
        print("The response of SubjectsApi->get_subjects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->get_subjects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| ID of the school to retrieve subjects for | 
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **include** | **str**| Comma separated list of objects to include. | [optional] 
 **subject_code** | **str**| Return results with the provided subject code. | [optional] 
 **subject_name** | **str**| Return results with the provided subject name. | [optional] 

### Return type

[**GetSubjects200Response**](GetSubjects200Response.md)

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

