# wonde.SchoolsApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_school**](SchoolsApi.md#get_school) | **GET** /schools/{school_id} | Retrieve a specific school
[**meta_schools_school_id_get**](SchoolsApi.md#meta_schools_school_id_get) | **GET** /meta/schools/{school_id} | Retrieve meta data for a school
[**meta_schools_school_id_permissions_get**](SchoolsApi.md#meta_schools_school_id_permissions_get) | **GET** /meta/schools/{school_id}/permissions | Retrieve the permissions applied to a school
[**schools_all_get**](SchoolsApi.md#schools_all_get) | **GET** /schools/all | Retrieve all schools
[**schools_approved_get**](SchoolsApi.md#schools_approved_get) | **GET** /schools/approved | Retrieve all approved schools
[**schools_audited_get**](SchoolsApi.md#schools_audited_get) | **GET** /schools/audited | Retrieve all audited schools
[**schools_declined_get**](SchoolsApi.md#schools_declined_get) | **GET** /schools/declined | Retrieve all schools with declined access
[**schools_offline_get**](SchoolsApi.md#schools_offline_get) | **GET** /schools/offline | Retrieve all offline schools
[**schools_pending_get**](SchoolsApi.md#schools_pending_get) | **GET** /schools/pending | Retrieve all schools with pending access request
[**schools_revoked_get**](SchoolsApi.md#schools_revoked_get) | **GET** /schools/revoked | Retrieve all schools with revoked access
[**schools_school_id_request_access_post**](SchoolsApi.md#schools_school_id_request_access_post) | **POST** /schools/{school_id}/request-access | Request access to a school
[**schools_school_id_revoke_access_delete**](SchoolsApi.md#schools_school_id_revoke_access_delete) | **DELETE** /schools/{school_id}/revoke-access | Revoke access to a school


# **get_school**
> School get_school(school_id)

Retrieve a specific school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.school import School
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

[**School**](School.md)

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

# **meta_schools_school_id_get**
> MetaSchoolsSchoolIdGet200Response meta_schools_school_id_get(school_id)

Retrieve meta data for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.meta_schools_school_id_get200_response import MetaSchoolsSchoolIdGet200Response
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
        api_response = api_instance.meta_schools_school_id_get(school_id)
        print("The response of SchoolsApi->meta_schools_school_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->meta_schools_school_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 

### Return type

[**MetaSchoolsSchoolIdGet200Response**](MetaSchoolsSchoolIdGet200Response.md)

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

# **meta_schools_school_id_permissions_get**
> MetaSchoolsSchoolIdPermissionsGet200Response meta_schools_school_id_permissions_get(school_id)

Retrieve the permissions applied to a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.meta_schools_school_id_permissions_get200_response import MetaSchoolsSchoolIdPermissionsGet200Response
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
        api_response = api_instance.meta_schools_school_id_permissions_get(school_id)
        print("The response of SchoolsApi->meta_schools_school_id_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->meta_schools_school_id_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 

### Return type

[**MetaSchoolsSchoolIdPermissionsGet200Response**](MetaSchoolsSchoolIdPermissionsGet200Response.md)

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

# **schools_all_get**
> SchoolsAllGet200Response schools_all_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        # Retrieve all schools
        api_response = api_instance.schools_all_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->schools_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_all_get: %s\n" % e)
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

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_approved_get**
> SchoolsAllGet200Response schools_approved_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all approved schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        # Retrieve all approved schools
        api_response = api_instance.schools_approved_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->schools_approved_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_approved_get: %s\n" % e)
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

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_audited_get**
> SchoolsAllGet200Response schools_audited_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all audited schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        # Retrieve all audited schools
        api_response = api_instance.schools_audited_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->schools_audited_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_audited_get: %s\n" % e)
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

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_declined_get**
> SchoolsAllGet200Response schools_declined_get(per_page=per_page)

Retrieve all schools with declined access

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        api_response = api_instance.schools_declined_get(per_page=per_page)
        print("The response of SchoolsApi->schools_declined_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_declined_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Amount of rows to return | [optional] 

### Return type

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_offline_get**
> SchoolsAllGet200Response schools_offline_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all offline schools

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        api_response = api_instance.schools_offline_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->schools_offline_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_offline_get: %s\n" % e)
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

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_pending_get**
> SchoolsAllGet200Response schools_pending_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)

Retrieve all schools with pending access request

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        # Retrieve all schools with pending access request
        api_response = api_instance.schools_pending_get(updated_after=updated_after, updated_before=updated_before, per_page=per_page, postcode=postcode, la_code=la_code, establishment_number=establishment_number, urn=urn)
        print("The response of SchoolsApi->schools_pending_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_pending_get: %s\n" % e)
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

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_revoked_get**
> SchoolsAllGet200Response schools_revoked_get(per_page=per_page)

Retrieve all schools with revoked access

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response
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
        api_response = api_instance.schools_revoked_get(per_page=per_page)
        print("The response of SchoolsApi->schools_revoked_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_revoked_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Amount of rows to return | [optional] 

### Return type

[**SchoolsAllGet200Response**](SchoolsAllGet200Response.md)

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

# **schools_school_id_request_access_post**
> SchoolsSchoolIdRequestAccessPost200Response schools_school_id_request_access_post(school_id, schools_school_id_request_access_post_request=schools_school_id_request_access_post_request)

Request access to a school

When requesting access to a school it is recommended that you provide details of available  contacts at the school.  This can speed up the approval process considerably but it is not required.  The contact should be provided within an array.  More than one contact can be provided. 

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_school_id_request_access_post200_response import SchoolsSchoolIdRequestAccessPost200Response
from wonde.models.schools_school_id_request_access_post_request import SchoolsSchoolIdRequestAccessPostRequest
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
    schools_school_id_request_access_post_request = wonde.SchoolsSchoolIdRequestAccessPostRequest() # SchoolsSchoolIdRequestAccessPostRequest | Contacts to add for the request (optional)

    try:
        # Request access to a school
        api_response = api_instance.schools_school_id_request_access_post(school_id, schools_school_id_request_access_post_request=schools_school_id_request_access_post_request)
        print("The response of SchoolsApi->schools_school_id_request_access_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_school_id_request_access_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **schools_school_id_request_access_post_request** | [**SchoolsSchoolIdRequestAccessPostRequest**](SchoolsSchoolIdRequestAccessPostRequest.md)| Contacts to add for the request | [optional] 

### Return type

[**SchoolsSchoolIdRequestAccessPost200Response**](SchoolsSchoolIdRequestAccessPost200Response.md)

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

# **schools_school_id_revoke_access_delete**
> SchoolsSchoolIdRequestAccessPost200Response schools_school_id_revoke_access_delete(school_id)

Revoke access to a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_school_id_request_access_post200_response import SchoolsSchoolIdRequestAccessPost200Response
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
        api_response = api_instance.schools_school_id_revoke_access_delete(school_id)
        print("The response of SchoolsApi->schools_school_id_revoke_access_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->schools_school_id_revoke_access_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 

### Return type

[**SchoolsSchoolIdRequestAccessPost200Response**](SchoolsSchoolIdRequestAccessPost200Response.md)

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

