# SchoolClassLessons


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Lesson]**](Lesson.md) |  | [optional] 

## Example

```python
from wonde.models.school_class_lessons import SchoolClassLessons

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolClassLessons from a JSON string
school_class_lessons_instance = SchoolClassLessons.from_json(json)
# print the JSON string representation of the object
print SchoolClassLessons.to_json()

# convert the object into a dict
school_class_lessons_dict = school_class_lessons_instance.to_dict()
# create an instance of SchoolClassLessons from a dict
school_class_lessons_form_dict = school_class_lessons.from_dict(school_class_lessons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


