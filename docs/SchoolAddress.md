# SchoolAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line_1** | **str** |  | [optional] 
**address_line_2** | **str** |  | [optional] 
**address_town** | **str** |  | [optional] 
**address_postcode** | **str** |  | [optional] 
**address_country** | [**SchoolAddressAddressCountry**](SchoolAddressAddressCountry.md) |  | [optional] 

## Example

```python
from wonde.models.school_address import SchoolAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolAddress from a JSON string
school_address_instance = SchoolAddress.from_json(json)
# print the JSON string representation of the object
print SchoolAddress.to_json()

# convert the object into a dict
school_address_dict = school_address_instance.to_dict()
# create an instance of SchoolAddress from a dict
school_address_form_dict = school_address.from_dict(school_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


