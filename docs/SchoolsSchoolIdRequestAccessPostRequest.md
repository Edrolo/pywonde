# SchoolsSchoolIdRequestAccessPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 

## Example

```python
from wonde.models.schools_school_id_request_access_post_request import SchoolsSchoolIdRequestAccessPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolsSchoolIdRequestAccessPostRequest from a JSON string
schools_school_id_request_access_post_request_instance = SchoolsSchoolIdRequestAccessPostRequest.from_json(json)
# print the JSON string representation of the object
print SchoolsSchoolIdRequestAccessPostRequest.to_json()

# convert the object into a dict
schools_school_id_request_access_post_request_dict = schools_school_id_request_access_post_request_instance.to_dict()
# create an instance of SchoolsSchoolIdRequestAccessPostRequest from a dict
schools_school_id_request_access_post_request_form_dict = schools_school_id_request_access_post_request.from_dict(schools_school_id_request_access_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


