# wonde.EmployeesApi

All URIs are relative to *https://api.wonde.com/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schools_school_id_employees_employee_id_get**](EmployeesApi.md#schools_school_id_employees_employee_id_get) | **GET** /schools/{school_id}/employees/{employee_id} | Get specific employee for a school
[**schools_school_id_employees_get**](EmployeesApi.md#schools_school_id_employees_get) | **GET** /schools/{school_id}/employees | Get all employees for a school


# **schools_school_id_employees_employee_id_get**
> Employee schools_school_id_employees_employee_id_get(school_id, employee_id)

Get specific employee for a school

You need the employees read permission to view this object. To retrieve the secondary and tertiary ids please add extra_ids=true to the url. 

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.employee import Employee
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
    api_instance = wonde.EmployeesApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    employee_id = 'employee_id_example' # str | The ID of the employee

    try:
        # Get specific employee for a school
        api_response = api_instance.schools_school_id_employees_employee_id_get(school_id, employee_id)
        print("The response of EmployeesApi->schools_school_id_employees_employee_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schools_school_id_employees_employee_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **employee_id** | **str**| The ID of the employee | 

### Return type

[**Employee**](Employee.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An employee for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schools_school_id_employees_get**
> SchoolsSchoolIdEmployeesGet200Response schools_school_id_employees_get(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, employment_start_before=employment_start_before, employment_start_after=employment_start_after, has_role=has_role, has_contract=has_contract, has_class=has_class, has_group=has_group, user_defined_field=user_defined_field, only_user_defined_fields=only_user_defined_fields, only_mis_ids=only_mis_ids)

Get all employees for a school

### Example

* Basic Authentication (BasicAuth):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import wonde
from wonde.models.schools_school_id_employees_get200_response import SchoolsSchoolIdEmployeesGet200Response
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
    api_instance = wonde.EmployeesApi(api_client)
    school_id = 'school_id_example' # str | The ID of the school
    updated_after = '2013-10-20' # date | Return rows modified after date (optional)
    updated_before = '2013-10-20' # date | Return rows modified before date (optional)
    per_page = 56 # int | Amount of rows to return (optional)
    include = 'include_example' # str | Comma separated list of objects to include (optional)
    employment_start_before = '2013-10-20' # date | Get employees who have started before a date (optional)
    employment_start_after = '2013-10-20' # date | Get employees who have started after a date (optional)
    has_role = True # bool | Only return employees that have a role (optional)
    has_contract = True # bool | Only return employees that have a contract (optional)
    has_class = True # bool | Only return employees that have one or more classes (optional)
    has_group = True # bool | Only return employees that have one or more groups (optional)
    user_defined_field = 'user_defined_field_example' # str | Filter employees by user defined field key (optional)
    only_user_defined_fields = 'only_user_defined_fields_example' # str | Filter user defined fields by comma separated list (optional)
    only_mis_ids = 'only_mis_ids_example' # str | Filter MIS ids by comma separated list (optional)

    try:
        # Get all employees for a school
        api_response = api_instance.schools_school_id_employees_get(school_id, updated_after=updated_after, updated_before=updated_before, per_page=per_page, include=include, employment_start_before=employment_start_before, employment_start_after=employment_start_after, has_role=has_role, has_contract=has_contract, has_class=has_class, has_group=has_group, user_defined_field=user_defined_field, only_user_defined_fields=only_user_defined_fields, only_mis_ids=only_mis_ids)
        print("The response of EmployeesApi->schools_school_id_employees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->schools_school_id_employees_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **str**| The ID of the school | 
 **updated_after** | **date**| Return rows modified after date | [optional] 
 **updated_before** | **date**| Return rows modified before date | [optional] 
 **per_page** | **int**| Amount of rows to return | [optional] 
 **include** | **str**| Comma separated list of objects to include | [optional] 
 **employment_start_before** | **date**| Get employees who have started before a date | [optional] 
 **employment_start_after** | **date**| Get employees who have started after a date | [optional] 
 **has_role** | **bool**| Only return employees that have a role | [optional] 
 **has_contract** | **bool**| Only return employees that have a contract | [optional] 
 **has_class** | **bool**| Only return employees that have one or more classes | [optional] 
 **has_group** | **bool**| Only return employees that have one or more groups | [optional] 
 **user_defined_field** | **str**| Filter employees by user defined field key | [optional] 
 **only_user_defined_fields** | **str**| Filter user defined fields by comma separated list | [optional] 
 **only_mis_ids** | **str**| Filter MIS ids by comma separated list | [optional] 

### Return type

[**SchoolsSchoolIdEmployeesGet200Response**](SchoolsSchoolIdEmployeesGet200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of employees for a specific school |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

