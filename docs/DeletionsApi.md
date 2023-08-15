# wonde.DeletionsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_school_deletions**](DeletionsApi.md#list_school_deletions) | **GET** /schools/{school_id}/deletions | Get deletions for a school


# **list_school_deletions**
> ListSchoolDeletions200Response list_school_deletions(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, type=type)

Get deletions for a school

It's recommended that you use the updated_after url parameter to efficiently sync updates  to datasets. The deletions endpoint exists to provide a record of when an item is deleted.  The deletions endpoint will have an entry for every top level item (student, contact,  employee, group...) unless the object is deleted due to a parent being removed. An example of this would be when a class is removed the associated lessons would be deleted without an entry in the deletions endpoint. A `restored_at` value will be returned for the deletions of students, student pre-admissions,  student leavers, contacts, employees, groups and classes when a record that was previously  deleted has been restored (it became available in the MIS data again with the same MIS ID). It's recommended that applications perform frequent full syncs to make sure data remains accurate. 

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_school_deletions200_response import ListSchoolDeletions200Response
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
    api_instance = wonde.DeletionsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    type = 'type_example' # str | Only return records that have the provided type (optional)

    try:
        # Get deletions for a school
        api_response = api_instance.list_school_deletions(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, type=type)
        print("The response of DeletionsApi->list_school_deletions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionsApi->list_school_deletions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **type** | **str**| Only return records that have the provided type | [optional] 

### Return type

[**ListSchoolDeletions200Response**](ListSchoolDeletions200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of deletions for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

