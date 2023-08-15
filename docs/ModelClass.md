# ModelClass

https://docs.wonde.com/docs/api/sync#get-classes Related objects Name                            Relationship -------------------------------------------- subject                         one students                        many students.contact_details        many > one students.education_details      many > one students.extended_details       many > one students.house                  many > one students.registration           many > one students.year                   many > one students.boarding               many > one students.campus                 many > one employees                       many employees.contact_details       many > one employees.employment_details    many > one employees.extended_details      many > one lessons                         many lessons.room                    many > one lessons.period                  many > one 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**mis_id** | **str** | The ID in the MIS. | [optional] 
**name** | **str** | Class name. | [optional] 
**code** | **str** | Class code. | [optional] 
**description** | **str** | Class description. | [optional] 
**subject** | **str** | The subject for the class. | [optional] 
**alternative** | **bool** | The class is an alternative to another class. | [optional] 
**restored_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 

## Example

```python
from wonde.models.model_class import ModelClass

# TODO update the JSON string below
json = "{}"
# create an instance of ModelClass from a JSON string
model_class_instance = ModelClass.from_json(json)
# print the JSON string representation of the object
print ModelClass.to_json()

# convert the object into a dict
model_class_dict = model_class_instance.to_dict()
# create an instance of ModelClass from a dict
model_class_form_dict = model_class.from_dict(model_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


