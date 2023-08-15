# School


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**establishment_number** | **int** |  | [optional] 
**urn** | **int** |  | [optional] 
**phase_of_education** | **str** |  | [optional] 
**la_code** | **int** |  | [optional] 
**timezone** | **str** |  | [optional] 
**mis** | **str** |  | [optional] 
**address** | [**SchoolAddress**](SchoolAddress.md) |  | [optional] 
**extended** | [**SchoolExtended**](SchoolExtended.md) |  | [optional] 
**region** | [**SchoolRegion**](SchoolRegion.md) |  | [optional] 

## Example

```python
from wonde.models.school import School

# TODO update the JSON string below
json = "{}"
# create an instance of School from a JSON string
school_instance = School.from_json(json)
# print the JSON string representation of the object
print School.to_json()

# convert the object into a dict
school_dict = school_instance.to_dict()
# create an instance of School from a dict
school_form_dict = school.from_dict(school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


