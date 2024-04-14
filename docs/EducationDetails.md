# EducationDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_nc_year** | **str** |  | [optional] 
**local_upn** | **str** |  | [optional] 

## Example

```python
from wonde.models.education_details import EducationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EducationDetails from a JSON string
education_details_instance = EducationDetails.from_json(json)
# print the JSON string representation of the object
print EducationDetails.to_json()

# convert the object into a dict
education_details_dict = education_details_instance.to_dict()
# create an instance of EducationDetails from a dict
education_details_form_dict = education_details.from_dict(education_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


