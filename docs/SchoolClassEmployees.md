# SchoolClassEmployees


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Employee]**](Employee.md) |  | [optional] 

## Example

```python
from wonde.models.school_class_employees import SchoolClassEmployees

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolClassEmployees from a JSON string
school_class_employees_instance = SchoolClassEmployees.from_json(json)
# print the JSON string representation of the object
print SchoolClassEmployees.to_json()

# convert the object into a dict
school_class_employees_dict = school_class_employees_instance.to_dict()
# create an instance of SchoolClassEmployees from a dict
school_class_employees_form_dict = school_class_employees.from_dict(school_class_employees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


