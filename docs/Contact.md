# Contact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of contact | [optional] 
**last_name** | **str** | Last name of contact | [optional] 
**phone_number** | **str** | Phone number of contact | [optional] 
**email_address** | **str** | Email address of contact | [optional] 
**notes** | **str** | Notes for the contact | [optional] 

## Example

```python
from wonde.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print Contact.to_json()

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_form_dict = contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


