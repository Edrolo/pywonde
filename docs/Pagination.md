# Pagination

https://docs.wonde.com/docs/api/sync#pagination The pagination object is returned as part of the response body when pagination is enabled.  By default, 50 objects are returned per page. If the response contains 50 objects or fewer,  no pagination object will be returned. If the response contains more than 50 objects, the  first 50 will be returned along with the pagination object. You can request a different pagination limit or force pagination by appending ?per_page= to  the request with the number of items you would like per page. For instance, to show only two  results per page, you could add ?per_page=2 to the end of your query.  The maximum number of results per page is set per-endpoint. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The next page in the paginated response. | [optional] 
**previous** | **str** | The previous page in the paginated response. | [optional] 
**more** | **bool** | Is there another page after the current page. | [optional] 
**per_page** | **int** | How many rows are currently being returned per page/response. | [optional] 
**current_page** | **int** | The current paginated page number. | [optional] 

## Example

```python
from wonde.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print Pagination.to_json()

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_form_dict = pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


