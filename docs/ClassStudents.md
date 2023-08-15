# ClassStudents


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Student]**](Student.md) |  | [optional] 

## Example

```python
from wonde.models.class_students import ClassStudents

# TODO update the JSON string below
json = "{}"
# create an instance of ClassStudents from a JSON string
class_students_instance = ClassStudents.from_json(json)
# print the JSON string representation of the object
print ClassStudents.to_json()

# convert the object into a dict
class_students_dict = class_students_instance.to_dict()
# create an instance of ClassStudents from a dict
class_students_form_dict = class_students.from_dict(class_students_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


