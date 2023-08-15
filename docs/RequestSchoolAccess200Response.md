# RequestSchoolAccess200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from wonde.models.request_school_access200_response import RequestSchoolAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSchoolAccess200Response from a JSON string
request_school_access200_response_instance = RequestSchoolAccess200Response.from_json(json)
# print the JSON string representation of the object
print RequestSchoolAccess200Response.to_json()

# convert the object into a dict
request_school_access200_response_dict = request_school_access200_response_instance.to_dict()
# create an instance of RequestSchoolAccess200Response from a dict
request_school_access200_response_form_dict = request_school_access200_response.from_dict(request_school_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


