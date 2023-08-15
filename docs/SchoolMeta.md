# SchoolMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online** | **bool** | If the school is online | [optional] 
**approved** | **bool** | If the school has approved access to application | [optional] 
**audited** | **bool** | If the school has been audited for data completeness | [optional] 
**custom_attendance_codes** | **bool** | If the school has their own custom attendance codes | [optional] 

## Example

```python
from wonde.models.school_meta import SchoolMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolMeta from a JSON string
school_meta_instance = SchoolMeta.from_json(json)
# print the JSON string representation of the object
print SchoolMeta.to_json()

# convert the object into a dict
school_meta_dict = school_meta_instance.to_dict()
# create an instance of SchoolMeta from a dict
school_meta_form_dict = school_meta.from_dict(school_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


