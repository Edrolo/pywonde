# SchoolClassStudents


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Student]**](Student.md) |  | [optional] 

## Example

```python
from wonde.models.school_class_students import SchoolClassStudents

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolClassStudents from a JSON string
school_class_students_instance = SchoolClassStudents.from_json(json)
# print the JSON string representation of the object
print SchoolClassStudents.to_json()

# convert the object into a dict
school_class_students_dict = school_class_students_instance.to_dict()
# create an instance of SchoolClassStudents from a dict
school_class_students_form_dict = school_class_students.from_dict(school_class_students_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


