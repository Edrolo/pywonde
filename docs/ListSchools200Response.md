# ListSchools200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[School]**](School.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from wonde.models.list_schools200_response import ListSchools200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSchools200Response from a JSON string
list_schools200_response_instance = ListSchools200Response.from_json(json)
# print the JSON string representation of the object
print ListSchools200Response.to_json()

# convert the object into a dict
list_schools200_response_dict = list_schools200_response_instance.to_dict()
# create an instance of ListSchools200Response from a dict
list_schools200_response_form_dict = list_schools200_response.from_dict(list_schools200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


