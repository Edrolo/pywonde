# wonde.SchoolsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_school**](SchoolsApi.md#get_school) | **GET** /schools/{school_id} | Retrieve a specific school
[**get_school_acl**](SchoolsApi.md#get_school_acl) | **GET** /meta/schools/{school_id}/acl | Retrieve the access control list applied to a school
[**get_school_meta**](SchoolsApi.md#get_school_meta) | **GET** /meta/schools/{school_id} | Retrieve meta data for a school
[**get_school_permissions**](SchoolsApi.md#get_school_permissions) | **GET** /meta/schools/{school_id}/permissions | Retrieve the permissions applied to a school
[**list_schools**](SchoolsApi.md#list_schools) | **GET** /schools/all | Retrieve all schools
[**list_schools_approved**](SchoolsApi.md#list_schools_approved) | **GET** /schools | Retrieve all approved schools
[**list_schools_audited**](SchoolsApi.md#list_schools_audited) | **GET** /schools/audited | Retrieve all audited schools
[**list_schools_declined**](SchoolsApi.md#list_schools_declined) | **GET** /schools/declined | Retrieve all schools with declined access
[**list_schools_offline**](SchoolsApi.md#list_schools_offline) | **GET** /schools/offline | Retrieve all offline schools
[**list_schools_pending**](SchoolsApi.md#list_schools_pending) | **GET** /schools/pending | Retrieve all schools with pending access request
[**list_schools_revoked**](SchoolsApi.md#list_schools_revoked) | **GET** /schools/revoked | Retrieve all schools with revoked access
[**request_school_access**](SchoolsApi.md#request_school_access) | **POST** /schools/{school_id}/request-access | Request access to a school
[**revoke_school_access**](SchoolsApi.md#revoke_school_access) | **DELETE** /schools/{school_id}/revoke-access | Revoke access to a school


# **get_school**
> GetSchool200Response get_school(school_id)

Retrieve a specific school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.get_school200_response import GetSchool200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school to retrieve

    try:
        # Retrieve a specific school
        api_response = api_instance.get_school(school_id)
        print("The response of SchoolsApi->get_school:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->get_school: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school to retrieve | 

### Return type

[**GetSchool200Response**](GetSchool200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_acl**
> GetSchoolAcl200Response get_school_acl(school_id, with_user_type=with_user_type)

Retrieve the access control list applied to a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.get_school_acl200_response import GetSchoolAcl200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    with_user_type = True # bool | Display the type of user (optional)

    try:
        # Retrieve the access control list applied to a school
        api_response = api_instance.get_school_acl(school_id, with_user_type=with_user_type)
        print("The response of SchoolsApi->get_school_acl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->get_school_acl: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **with_user_type** | **bool**| Display the type of user | [optional] 

### Return type

[**GetSchoolAcl200Response**](GetSchoolAcl200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access control list for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_meta**
> GetSchoolMeta200Response get_school_meta(school_id)

Retrieve meta data for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.get_school_meta200_response import GetSchoolMeta200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school

    try:
        # Retrieve meta data for a school
        api_response = api_instance.get_school_meta(school_id)
        print("The response of SchoolsApi->get_school_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->get_school_meta: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 

### Return type

[**GetSchoolMeta200Response**](GetSchoolMeta200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meta data for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_permissions**
> GetSchoolPermissions200Response get_school_permissions(school_id)

Retrieve the permissions applied to a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.get_school_permissions200_response import GetSchoolPermissions200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school

    try:
        # Retrieve the permissions applied to a school
        api_response = api_instance.get_school_permissions(school_id)
        print("The response of SchoolsApi->get_school_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->get_school_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 

### Return type

[**GetSchoolPermissions200Response**](GetSchoolPermissions200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions applied to a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools**
> ListSchools200Response list_schools(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    page = 56 # int | Page offset for offset-paginated results. (optional)
    cursor = 'cursor_example' # str | Page cursor for cursor-paginated results. (optional)
    postcode = 'postcode_example' # str | Return results matching postcode search string (optional)
    la_code = 'la_code_example' # str | Return results with provided la_code (optional)
    establishment_number = 'establishment_number_example' # str | Return results with provided establishment_number (optional)
    urn = 56 # int | Return results with provided unique reference number (optional)

    try:
        # Retrieve all schools
        api_response = api_instance.list_schools(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->list_schools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **page** | **int**| Page offset for offset-paginated results. | [optional] 
 **cursor** | **str**| Page cursor for cursor-paginated results. | [optional] 
 **postcode** | **str**| Return results matching postcode search string | [optional] 
 **la_code** | **str**| Return results with provided la_code | [optional] 
 **establishment_number** | **str**| Return results with provided establishment_number | [optional] 
 **urn** | **int**| Return results with provided unique reference number | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools_approved**
> ListSchools200Response list_schools_approved(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all approved schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    page = 56 # int | Page offset for offset-paginated results. (optional)
    cursor = 'cursor_example' # str | Page cursor for cursor-paginated results. (optional)
    postcode = 'postcode_example' # str | Return results matching postcode search string (optional)
    la_code = 'la_code_example' # str | Return results with provided la_code (optional)
    establishment_number = 'establishment_number_example' # str | Return results with provided establishment_number (optional)
    urn = 56 # int | Return results with provided unique reference number (optional)

    try:
        # Retrieve all approved schools
        api_response = api_instance.list_schools_approved(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->list_schools_approved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools_approved: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **page** | **int**| Page offset for offset-paginated results. | [optional] 
 **cursor** | **str**| Page cursor for cursor-paginated results. | [optional] 
 **postcode** | **str**| Return results matching postcode search string | [optional] 
 **la_code** | **str**| Return results with provided la_code | [optional] 
 **establishment_number** | **str**| Return results with provided establishment_number | [optional] 
 **urn** | **int**| Return results with provided unique reference number | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools_audited**
> ListSchools200Response list_schools_audited(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all audited schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    page = 56 # int | Page offset for offset-paginated results. (optional)
    cursor = 'cursor_example' # str | Page cursor for cursor-paginated results. (optional)
    postcode = 'postcode_example' # str | Return results matching postcode search string (optional)
    la_code = 'la_code_example' # str | Return results with provided la_code (optional)
    establishment_number = 'establishment_number_example' # str | Return results with provided establishment_number (optional)
    urn = 56 # int | Return results with provided unique reference number (optional)

    try:
        # Retrieve all audited schools
        api_response = api_instance.list_schools_audited(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->list_schools_audited:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools_audited: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **page** | **int**| Page offset for offset-paginated results. | [optional] 
 **cursor** | **str**| Page cursor for cursor-paginated results. | [optional] 
 **postcode** | **str**| Return results matching postcode search string | [optional] 
 **la_code** | **str**| Return results with provided la_code | [optional] 
 **establishment_number** | **str**| Return results with provided establishment_number | [optional] 
 **urn** | **int**| Return results with provided unique reference number | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools_declined**
> ListSchools200Response list_schools_declined(per_page=per_page)

Retrieve all schools with declined access

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    per_page = 56 # int | Amount of rows to return (optional)

    try:
        # Retrieve all schools with declined access
        api_response = api_instance.list_schools_declined(per_page=per_page)
        print("The response of SchoolsApi->list_schools_declined:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools_declined: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Amount of rows to return | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools_offline**
> ListSchools200Response list_schools_offline(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all offline schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    postcode = 'postcode_example' # str | Return results matching postcode search string (optional)
    la_code = 'la_code_example' # str | Return results with provided la_code (optional)
    establishment_number = 'establishment_number_example' # str | Return results with provided establishment_number (optional)
    urn = 56 # int | Return results with provided unique reference number (optional)

    try:
        # Retrieve all offline schools
        api_response = api_instance.list_schools_offline(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->list_schools_offline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools_offline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **postcode** | **str**| Return results matching postcode search string | [optional] 
 **la_code** | **str**| Return results with provided la_code | [optional] 
 **establishment_number** | **str**| Return results with provided establishment_number | [optional] 
 **urn** | **int**| Return results with provided unique reference number | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools_pending**
> ListSchools200Response list_schools_pending(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all schools with pending access request

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    page = 56 # int | Page offset for offset-paginated results. (optional)
    cursor = 'cursor_example' # str | Page cursor for cursor-paginated results. (optional)
    postcode = 'postcode_example' # str | Return results matching postcode search string (optional)
    la_code = 'la_code_example' # str | Return results with provided la_code (optional)
    establishment_number = 'establishment_number_example' # str | Return results with provided establishment_number (optional)
    urn = 56 # int | Return results with provided unique reference number (optional)

    try:
        # Retrieve all schools with pending access request
        api_response = api_instance.list_schools_pending(updated_after=updated_after, updated_before=updated_before, per_page=per_page, page=page, cursor=cursor, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->list_schools_pending:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools_pending: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **page** | **int**| Page offset for offset-paginated results. | [optional] 
 **cursor** | **str**| Page cursor for cursor-paginated results. | [optional] 
 **postcode** | **str**| Return results matching postcode search string | [optional] 
 **la_code** | **str**| Return results with provided la_code | [optional] 
 **establishment_number** | **str**| Return results with provided establishment_number | [optional] 
 **urn** | **int**| Return results with provided unique reference number | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schools_revoked**
> ListSchools200Response list_schools_revoked(per_page=per_page)

Retrieve all schools with revoked access

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.list_schools200_response import ListSchools200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    per_page = 56 # int | Amount of rows to return (optional)

    try:
        # Retrieve all schools with revoked access
        api_response = api_instance.list_schools_revoked(per_page=per_page)
        print("The response of SchoolsApi->list_schools_revoked:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->list_schools_revoked: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Amount of rows to return | [optional] 

### Return type

[**ListSchools200Response**](ListSchools200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schools |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_school_access**
> RequestSchoolAccess200Response request_school_access(school_id, request_school_access_request=request_school_access_request)

Request access to a school

When requesting access to a school it is recommended that you provide details of available  contacts at the school.  This can speed up the approval process considerably but it is not required.  The contact should be provided within an array.  More than one contact can be provided. 

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.request_school_access200_response import RequestSchoolAccess200Response
from wonde.models.request_school_access_request import RequestSchoolAccessRequest
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
    api_instance = wonde.SchoolsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    request_school_access_request = wonde.RequestSchoolAccessRequest() # RequestSchoolAccessRequest | Contacts to add for the request (optional)

    try:
        # Request access to a school
        api_response = api_instance.request_school_access(school_id, request_school_access_request=request_school_access_request)
        print("The response of SchoolsApi->request_school_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->request_school_access: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **request_school_access_request** | [**RequestSchoolAccessRequest**](RequestSchoolAccessRequest.md)| Contacts to add for the request | [optional] 

### Return type

[**RequestSchoolAccess200Response**](RequestSchoolAccess200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to the access request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_school_access**
> RequestSchoolAccess200Response revoke_school_access(school_id)

Revoke access to a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.request_school_access200_response import RequestSchoolAccess200Response
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
    api_instance = wonde.SchoolsApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school

    try:
        # Revoke access to a school
        api_response = api_instance.revoke_school_access(school_id)
        print("The response of SchoolsApi->revoke_school_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->revoke_school_access: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 

### Return type

[**RequestSchoolAccess200Response**](RequestSchoolAccess200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to the revoke access request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

