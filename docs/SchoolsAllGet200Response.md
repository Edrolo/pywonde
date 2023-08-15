# SchoolsAllGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[School]**](School.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from wonde.models.schools_all_get200_response import SchoolsAllGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolsAllGet200Response from a JSON string
schools_all_get200_response_instance = SchoolsAllGet200Response.from_json(json)
# print the JSON string representation of the object
print SchoolsAllGet200Response.to_json()

# convert the object into a dict
schools_all_get200_response_dict = schools_all_get200_response_instance.to_dict()
# create an instance of SchoolsAllGet200Response from a dict
schools_all_get200_response_form_dict = schools_all_get200_response.from_dict(schools_all_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


