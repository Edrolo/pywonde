# EmployeeEmploymentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EmploymentDetails**](EmploymentDetails.md) |  | [optional] 

## Example

```python
from wonde.models.employee_employment_details import EmployeeEmploymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeEmploymentDetails from a JSON string
employee_employment_details_instance = EmployeeEmploymentDetails.from_json(json)
# print the JSON string representation of the object
print EmployeeEmploymentDetails.to_json()

# convert the object into a dict
employee_employment_details_dict = employee_employment_details_instance.to_dict()
# create an instance of EmployeeEmploymentDetails from a dict
employee_employment_details_form_dict = employee_employment_details.from_dict(employee_employment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


