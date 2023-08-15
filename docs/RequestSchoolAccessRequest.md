# RequestSchoolAccessRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 

## Example

```python
from wonde.models.request_school_access_request import RequestSchoolAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSchoolAccessRequest from a JSON string
request_school_access_request_instance = RequestSchoolAccessRequest.from_json(json)
# print the JSON string representation of the object
print RequestSchoolAccessRequest.to_json()

# convert the object into a dict
request_school_access_request_dict = request_school_access_request_instance.to_dict()
# create an instance of RequestSchoolAccessRequest from a dict
request_school_access_request_form_dict = request_school_access_request.from_dict(request_school_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


