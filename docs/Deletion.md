# Deletion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mis_id** | **str** |  | [optional] 
**deleted_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**restored_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 

## Example

```python
from wonde.models.deletion import Deletion

# TODO update the JSON string below
json = "{}"
# create an instance of Deletion from a JSON string
deletion_instance = Deletion.from_json(json)
# print the JSON string representation of the object
print Deletion.to_json()

# convert the object into a dict
deletion_dict = deletion_instance.to_dict()
# create an instance of Deletion from a dict
deletion_form_dict = deletion.from_dict(deletion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


