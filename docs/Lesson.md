# Lesson

https://docs.wonde.com/docs/api/sync#lesson-object Related objects Name      Relationship ---------------------- period    one class     one employee  one room      one 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**room** | **str** | The ID of the room the lesson will be taught in. | [optional] 
**period** | **str** | The ID of the period the lesson occurs during. | [optional] 
**employee_id** | **str** | The ID of the main class teacher for this lesson. | [optional] 
**period_instance_id** | **int** | All lessons happening during the same period have the same period_instance_id.  This value can be used to match lessons and attendance as SIMS records a mark for a  period instance not a lesson instance.  | [optional] 
**alternative** | **bool** | The lesson is an alternative to another lesson. | [optional] 
**start_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**end_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 

## Example

```python
from wonde.models.lesson import Lesson

# TODO update the JSON string below
json = "{}"
# create an instance of Lesson from a JSON string
lesson_instance = Lesson.from_json(json)
# print the JSON string representation of the object
print Lesson.to_json()

# convert the object into a dict
lesson_dict = lesson_instance.to_dict()
# create an instance of Lesson from a dict
lesson_form_dict = lesson.from_dict(lesson_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


