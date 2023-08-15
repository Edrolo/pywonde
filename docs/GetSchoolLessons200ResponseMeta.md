# GetSchoolLessons200ResponseMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**includes** | **List[str]** |  | [optional] 

## Example

```python
from wonde.models.get_school_lessons200_response_meta import GetSchoolLessons200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetSchoolLessons200ResponseMeta from a JSON string
get_school_lessons200_response_meta_instance = GetSchoolLessons200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetSchoolLessons200ResponseMeta.to_json()

# convert the object into a dict
get_school_lessons200_response_meta_dict = get_school_lessons200_response_meta_instance.to_dict()
# create an instance of GetSchoolLessons200ResponseMeta from a dict
get_school_lessons200_response_meta_form_dict = get_school_lessons200_response_meta.from_dict(get_school_lessons200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


