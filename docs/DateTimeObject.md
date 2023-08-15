# DateTimeObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date and time value, apparently with no timezone | [optional] 
**timezone_type** | **int** | The type of the timezone, represented by an integer. Not sure of mapping. | [optional] 
**timezone** | **str** | The timezone in which the date and time is represented. | [optional] 

## Example

```python
from wonde.models.date_time_object import DateTimeObject

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeObject from a JSON string
date_time_object_instance = DateTimeObject.from_json(json)
# print the JSON string representation of the object
print DateTimeObject.to_json()

# convert the object into a dict
date_time_object_dict = date_time_object_instance.to_dict()
# create an instance of DateTimeObject from a dict
date_time_object_form_dict = date_time_object.from_dict(date_time_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


