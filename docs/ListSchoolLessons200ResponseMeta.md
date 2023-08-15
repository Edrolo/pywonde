# ListSchoolLessons200ResponseMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**includes** | **List[str]** |  | [optional] 

## Example

```python
from wonde.models.list_school_lessons200_response_meta import ListSchoolLessons200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ListSchoolLessons200ResponseMeta from a JSON string
list_school_lessons200_response_meta_instance = ListSchoolLessons200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print ListSchoolLessons200ResponseMeta.to_json()

# convert the object into a dict
list_school_lessons200_response_meta_dict = list_school_lessons200_response_meta_instance.to_dict()
# create an instance of ListSchoolLessons200ResponseMeta from a dict
list_school_lessons200_response_meta_form_dict = list_school_lessons200_response_meta.from_dict(list_school_lessons200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


