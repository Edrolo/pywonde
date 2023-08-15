# ListSchoolLessons200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Lesson]**](Lesson.md) |  | [optional] 
**meta** | [**ListSchoolLessons200ResponseMeta**](ListSchoolLessons200ResponseMeta.md) |  | [optional] 

## Example

```python
from wonde.models.list_school_lessons200_response import ListSchoolLessons200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSchoolLessons200Response from a JSON string
list_school_lessons200_response_instance = ListSchoolLessons200Response.from_json(json)
# print the JSON string representation of the object
print ListSchoolLessons200Response.to_json()

# convert the object into a dict
list_school_lessons200_response_dict = list_school_lessons200_response_instance.to_dict()
# create an instance of ListSchoolLessons200Response from a dict
list_school_lessons200_response_form_dict = list_school_lessons200_response.from_dict(list_school_lessons200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


