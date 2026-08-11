# ListSchoolGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Group]**](Group.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from wonde.models.list_school_groups200_response import ListSchoolGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSchoolGroups200Response from a JSON string
list_school_groups200_response_instance = ListSchoolGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListSchoolGroups200Response.to_json())

# convert the object into a dict
list_school_groups200_response_dict = list_school_groups200_response_instance.to_dict()
# create an instance of ListSchoolGroups200Response from a dict
list_school_groups200_response_from_dict = ListSchoolGroups200Response.from_dict(list_school_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


