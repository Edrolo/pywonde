# GetSchool200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**School**](School.md) |  | [optional] 

## Example

```python
from wonde.models.get_school200_response import GetSchool200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSchool200Response from a JSON string
get_school200_response_instance = GetSchool200Response.from_json(json)
# print the JSON string representation of the object
print GetSchool200Response.to_json()

# convert the object into a dict
get_school200_response_dict = get_school200_response_instance.to_dict()
# create an instance of GetSchool200Response from a dict
get_school200_response_form_dict = get_school200_response.from_dict(get_school200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


