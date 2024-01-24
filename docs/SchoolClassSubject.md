# SchoolClassSubject

The subject for the class. `include` to get object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Subject**](Subject.md) |  | [optional] 

## Example

```python
from wonde.models.school_class_subject import SchoolClassSubject

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolClassSubject from a JSON string
school_class_subject_instance = SchoolClassSubject.from_json(json)
# print the JSON string representation of the object
print SchoolClassSubject.to_json()

# convert the object into a dict
school_class_subject_dict = school_class_subject_instance.to_dict()
# create an instance of SchoolClassSubject from a dict
school_class_subject_form_dict = school_class_subject.from_dict(school_class_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


