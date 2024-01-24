# Student

https://docs.wonde.com/docs/api/sync#student-object You need the students read permission to view this object. Related objects Name                                Relationship ------------------------------------------------ classes                             many classes.employees                   many classes.subject                     many > one education_details                   one contact_details                     one attendance_summary                  one extended_details                    one contacts                            many contacts.contact_details            many > one year                                one (nullable) year.employees                      one (nullable) > many house                               one (nullable) house.employees                     one (nullable) > many registration                        one (nullable) registration.employees              one (nullable) > many boarding                            one (nullable) boarding.employees                  one (nullable) > many groups                              many groups.employees                    many > many campus                              one (nullable) permissions                         one identifiers                         one behaviours                          many behaviours.employees                many > many achievements                        many achievements.employees              many > many photo                               one sen_needs                           many siblings                            many medical_conditions                  many medical_conditions.notes            many > many medical_events                      many medical_events.notes                many > many medical_notes                       many doctors                             many in_care_date_ranges                 many sen_date_ranges                     many fsm_date_ranges                     many user_defined_fields                 many results                             many results.aspect                      many > one results.resultset                   many > one exclusions                          many child_protection_plan_date_ranges   many upfsm_date_ranges                   many 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the object. | [optional] 
**upi** | **str** | Unique Person Identifier - This field is the mis_id and school_id combined to create a unique hash. There are benefits of using the UPI when matching users, for example, when a student is dis-enrolled the student will be removed from Wonde. If that student is then re-enrolled the Wonde ID will change but the UPI will remain  the same.  Make sure to not mistake this field with UPN.  | [optional] 
**mis_id** | **str** | The student’s ID in the MIS. | [optional] 
**initials** | **str** | The student’s initials. | [optional] 
**surname** | **str** | The student’s last name. | [optional] 
**forename** | **str** | The student’s first name. | [optional] 
**middle_names** | **str** | The student’s middle names. | [optional] 
**legal_surname** | **str** | The student’s legal last name. | [optional] 
**legal_forename** | **str** | The student’s legal first name. | [optional] 
**gender** | **str** | The student’s gender. Possible values are &#39;MALE&#39; or &#39;FEMALE&#39;. | [optional] 
**date_of_birth** | **date** | Student&#39;s date of birth. | [optional] 
**restored_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**created_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**updated_at** | [**DateTimeObject**](DateTimeObject.md) |  | [optional] 
**contact_details** | [**EmployeeContactDetails**](EmployeeContactDetails.md) |  | [optional] 
**education_details** | [**StudentEducationDetails**](StudentEducationDetails.md) |  | [optional] 

## Example

```python
from wonde.models.student import Student

# TODO update the JSON string below
json = "{}"
# create an instance of Student from a JSON string
student_instance = Student.from_json(json)
# print the JSON string representation of the object
print Student.to_json()

# convert the object into a dict
student_dict = student_instance.to_dict()
# create an instance of Student from a dict
student_form_dict = student.from_dict(student_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


