# GetSchoolLessons200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Lesson]**](Lesson.md) |  | [optional] 
**meta** | [**GetSchoolLessons200ResponseMeta**](GetSchoolLessons200ResponseMeta.md) |  | [optional] 

## Example

```python
from wonde.models.get_school_lessons200_response import GetSchoolLessons200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSchoolLessons200Response from a JSON string
get_school_lessons200_response_instance = GetSchoolLessons200Response.from_json(json)
# print the JSON string representation of the object
print GetSchoolLessons200Response.to_json()

# convert the object into a dict
get_school_lessons200_response_dict = get_school_lessons200_response_instance.to_dict()
# create an instance of GetSchoolLessons200Response from a dict
get_school_lessons200_response_form_dict = get_school_lessons200_response.from_dict(get_school_lessons200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


