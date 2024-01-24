# StudentEducationDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EducationDetails**](EducationDetails.md) |  | [optional] 

## Example

```python
from wonde.models.student_education_details import StudentEducationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StudentEducationDetails from a JSON string
student_education_details_instance = StudentEducationDetails.from_json(json)
# print the JSON string representation of the object
print StudentEducationDetails.to_json()

# convert the object into a dict
student_education_details_dict = student_education_details_instance.to_dict()
# create an instance of StudentEducationDetails from a dict
student_education_details_form_dict = student_education_details.from_dict(student_education_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


