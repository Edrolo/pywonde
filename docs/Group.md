# Group

https://docs.wonde.com/docs/api/sync#group-object Campuses are modelled as groups with type=CAMPUS — Wonde has no campuses resource, and campus is only ever available as an `include` on groups, students and employees, never as a query filter. Related objects Name                 Relationship ----------------------------------- students             many employees            many 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**mis_id** | **str** | The group’s ID in the MIS. | [optional] 
**name** | **str** | Group name. | [optional] 
**code** | **str** | Group code. | [optional] 
**type** | **str** | The group type. One of REGISTRATION, YEAR, HOUSE, BOARDING, COURSE, MISC, USER, CAMPUS, DIVISION, DEPARTMENT.  | [optional] 
**description** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**restored_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**students** | [**SchoolClassStudents**](SchoolClassStudents.md) |  | [optional] 
**employees** | [**SchoolClassEmployees**](SchoolClassEmployees.md) |  | [optional] 

## Example

```python
from wonde.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


