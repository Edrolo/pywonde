# ClassLessons


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Lesson]**](Lesson.md) |  | [optional] 

## Example

```python
from wonde.models.class_lessons import ClassLessons

# TODO update the JSON string below
json = "{}"
# create an instance of ClassLessons from a JSON string
class_lessons_instance = ClassLessons.from_json(json)
# print the JSON string representation of the object
print ClassLessons.to_json()

# convert the object into a dict
class_lessons_dict = class_lessons_instance.to_dict()
# create an instance of ClassLessons from a dict
class_lessons_form_dict = class_lessons.from_dict(class_lessons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


