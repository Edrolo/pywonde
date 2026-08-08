# wonde.GroupsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_school_groups**](GroupsApi.md#list_school_groups) | **GET** /schools/{school_id}/groups | Get all groups for a school


# **list_school_groups**
> ListSchoolGroups200Response list_school_groups(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, include=include, type=type, has_students=has_students, has_employees=has_employees)

Get all groups for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):

```python
import wonde
from wonde.models.list_school_groups200_response import ListSchoolGroups200Response
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
    api_instance = wonde.GroupsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    page = 56 # int | Page offset for offset-paginated results. (optional)
    cursor = 'cursor_example' # str | Page cursor for cursor-paginated results. (optional)
    include = 'include_example' # str | Comma separated list of objects to include (optional)
    type = 'type_example' # str | Only return groups with the provided type. One of REGISTRATION, YEAR, HOUSE, BOARDING, COURSE, MISC, USER, CAMPUS, DIVISION, DEPARTMENT.  (optional)
    has_students = True # bool | Only return groups that have students (optional)
    has_employees = True # bool | Only return groups that have employees (optional)

    try:
        # Get all groups for a school
        api_response = api_instance.list_school_groups(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, include=include, type=type, has_students=has_students, has_employees=has_employees)
        print("The response of GroupsApi->list_school_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->list_school_groups: %s\n" % e)
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
 **type** | **str**| Only return groups with the provided type. One of REGISTRATION, YEAR, HOUSE, BOARDING, COURSE, MISC, USER, CAMPUS, DIVISION, DEPARTMENT.  | [optional] 
 **has_students** | **bool**| Only return groups that have students | [optional] 
 **has_employees** | **bool**| Only return groups that have employees | [optional] 

### Return type

[**ListSchoolGroups200Response**](ListSchoolGroups200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of groups for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

