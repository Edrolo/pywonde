# SchoolsSchoolIdClassesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelClass]**](ModelClass.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from wonde.models.schools_school_id_classes_get200_response import SchoolsSchoolIdClassesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolsSchoolIdClassesGet200Response from a JSON string
schools_school_id_classes_get200_response_instance = SchoolsSchoolIdClassesGet200Response.from_json(json)
# print the JSON string representation of the object
print SchoolsSchoolIdClassesGet200Response.to_json()

# convert the object into a dict
schools_school_id_classes_get200_response_dict = schools_school_id_classes_get200_response_instance.to_dict()
# create an instance of SchoolsSchoolIdClassesGet200Response from a dict
schools_school_id_classes_get200_response_form_dict = schools_school_id_classes_get200_response.from_dict(schools_school_id_classes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

