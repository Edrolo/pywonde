# ContactDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | [**ContactDetailsEmails**](ContactDetailsEmails.md) |  | [optional] 

## Example

```python
from wonde.models.contact_details import ContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetails from a JSON string
contact_details_instance = ContactDetails.from_json(json)
# print the JSON string representation of the object
print ContactDetails.to_json()

# convert the object into a dict
contact_details_dict = contact_details_instance.to_dict()
# create an instance of ContactDetails from a dict
contact_details_form_dict = contact_details.from_dict(contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


