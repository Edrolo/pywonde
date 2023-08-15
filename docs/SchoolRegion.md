# SchoolRegion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**school_url** | **str** |  | [optional] 
**identifiers** | [**SchoolRegionIdentifiers**](SchoolRegionIdentifiers.md) |  | [optional] 

## Example

```python
from wonde.models.school_region import SchoolRegion

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolRegion from a JSON string
school_region_instance = SchoolRegion.from_json(json)
# print the JSON string representation of the object
print SchoolRegion.to_json()

# convert the object into a dict
school_region_dict = school_region_instance.to_dict()
# create an instance of SchoolRegion from a dict
school_region_form_dict = school_region.from_dict(school_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


