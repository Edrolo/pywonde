# SchoolRegionIdentifiers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**la_code** | **str** |  | [optional] 
**establishment_number** | **str** |  | [optional] 
**urn** | **int** |  | [optional] 

## Example

```python
from wonde.models.school_region_identifiers import SchoolRegionIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolRegionIdentifiers from a JSON string
school_region_identifiers_instance = SchoolRegionIdentifiers.from_json(json)
# print the JSON string representation of the object
print SchoolRegionIdentifiers.to_json()

# convert the object into a dict
school_region_identifiers_dict = school_region_identifiers_instance.to_dict()
# create an instance of SchoolRegionIdentifiers from a dict
school_region_identifiers_form_dict = school_region_identifiers.from_dict(school_region_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


