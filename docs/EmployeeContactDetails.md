# EmployeeContactDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContactDetails**](ContactDetails.md) |  | [optional] 

## Example

```python
from wonde.models.employee_contact_details import EmployeeContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeContactDetails from a JSON string
employee_contact_details_instance = EmployeeContactDetails.from_json(json)
# print the JSON string representation of the object
print EmployeeContactDetails.to_json()

# convert the object into a dict
employee_contact_details_dict = employee_contact_details_instance.to_dict()
# create an instance of EmployeeContactDetails from a dict
employee_contact_details_form_dict = employee_contact_details.from_dict(employee_contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


