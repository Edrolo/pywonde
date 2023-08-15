# Subject

< https://docs.wonde.com/docs/api/sync#subject-object Related objects Name                    Relationship ----------------------------------------- classes                    many classes.lessons            many > many classes.lessons.period    many > many > one classes.lessons.room    many > many > one

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**mis_id** | **str** | The subject ID in the MIS. | [optional] 
**code** | **str** | Short identifier for the subject. | [optional] 
**name** | **str** | The subject’s name. | [optional] 
**active** | **bool** | Is the subject active. | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 

## Example

```python
from wonde.models.subject import Subject

# TODO update the JSON string below
json = "{}"
# create an instance of Subject from a JSON string
subject_instance = Subject.from_json(json)
# print the JSON string representation of the object
print Subject.to_json()

# convert the object into a dict
subject_dict = subject_instance.to_dict()
# create an instance of Subject from a dict
subject_form_dict = subject.from_dict(subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


