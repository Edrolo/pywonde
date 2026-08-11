# SchoolClass

https://docs.wonde.com/docs/api/sync#get-classes Related objects Name                            Relationship -------------------------------------------- subject                         one students                        many students.contact_details        many > one students.education_details      many > one students.extended_details       many > one students.house                  many > one students.registration           many > one students.year                   many > one students.boarding               many > one students.campus                 many > one employees                       many employees.contact_details       many > one employees.employment_details    many > one employees.extended_details      many > one lessons                         many lessons.room                    many > one lessons.period                  many > one 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**mis_id** | **str** | The ID in the MIS. | [optional] 
**type** | **str** | Class type. Australia region values: academic, duty, extra curricular, on call, roll class, rostered time off, staff meeting, study.  | [optional] 
**name** | **str** | Class name. | [optional] 
**code** | **str** | Class code. | [optional] 
**description** | **str** | Class description. | [optional] 
**subject** | [**SchoolClassSubject**](SchoolClassSubject.md) |  | [optional] 
**alternative** | **bool** | The class is an alternative to another class. | [optional] 
**priority** | **bool** | The class is a priority to another class. Supported in Edval and Timetabling Solutions data sync only.  | [optional] 
**academic_year** | **str** | The academic year of the class. Supported in SIMS, Edumate API and Synergetic data sync only.  | [optional] 
**year_group** | **str** | The year group of the class. Supported in SIMS only. | [optional] 
**restored_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**students** | [**SchoolClassStudents**](SchoolClassStudents.md) |  | [optional] 
**employees** | [**SchoolClassEmployees**](SchoolClassEmployees.md) |  | [optional] 
**lessons** | [**SchoolClassLessons**](SchoolClassLessons.md) |  | [optional] 

## Example

```python
from wonde.models.school_class import SchoolClass

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolClass from a JSON string
school_class_instance = SchoolClass.from_json(json)
# print the JSON string representation of the object
print(SchoolClass.to_json())

# convert the object into a dict
school_class_dict = school_class_instance.to_dict()
# create an instance of SchoolClass from a dict
school_class_from_dict = SchoolClass.from_dict(school_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


