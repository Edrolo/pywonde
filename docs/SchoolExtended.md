# SchoolExtended


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allows_writeback** | **bool** |  | [optional] 
**has_timetables** | **bool** |  | [optional] 
**has_lesson_attendance** | **bool** |  | [optional] 

## Example

```python
from wonde.models.school_extended import SchoolExtended

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolExtended from a JSON string
school_extended_instance = SchoolExtended.from_json(json)
# print the JSON string representation of the object
print SchoolExtended.to_json()

# convert the object into a dict
school_extended_dict = school_extended_instance.to_dict()
# create an instance of SchoolExtended from a dict
school_extended_form_dict = school_extended.from_dict(school_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


