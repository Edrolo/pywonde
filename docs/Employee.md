# Employee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**upi** | **str** | Unique Person Identifier - If a person is a contact and an employee they will have the same UPI but different ids. | [optional] 
**mis_id** | **str** | The ID in the Management Information System (MIS). | [optional] 
**title** | **str** | Employee&#39;s title. | [optional] 
**initials** | **str** | Employee&#39;s initials. | [optional] 
**surname** | **str** | Employee&#39;s surname. | [optional] 
**forename** | **str** | Employee&#39;s forename. | [optional] 
**middle_names** | **str** | Employee&#39;s middle names. | [optional] 
**legal_surname** | **str** | Employee&#39;s legal surname. | [optional] 
**legal_forename** | **str** | Employee&#39;s legal forename. | [optional] 
**gender** | **str** | Employee&#39;s gender. (male|female) | [optional] 
**date_of_birth** | **date** | Employee&#39;s date of birth. | [optional] 
**restored_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**contact_details** | [**EmployeeContactDetails**](EmployeeContactDetails.md) |  | [optional] 

## Example

```python
from wonde.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print Employee.to_json()

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_form_dict = employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


