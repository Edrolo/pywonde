# EmploymentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **bool** |  | [optional] 
**teaching_staff** | **bool** |  | [optional] 
**employment_start_date** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**employment_end_date** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**role_text** | **str** |  | [optional] 

## Example

```python
from wonde.models.employment_details import EmploymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EmploymentDetails from a JSON string
employment_details_instance = EmploymentDetails.from_json(json)
# print the JSON string representation of the object
print EmploymentDetails.to_json()

# convert the object into a dict
employment_details_dict = employment_details_instance.to_dict()
# create an instance of EmploymentDetails from a dict
employment_details_form_dict = employment_details.from_dict(employment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


