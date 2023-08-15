"""
Wonde API

API Docs  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401

from pydantic import BaseModel, conlist

from wonde.models.deletion import Deletion


class SchoolsSchoolIdDeletionsGet200Response(BaseModel):
    """
    SchoolsSchoolIdDeletionsGet200Response
    """

    data: conlist(Deletion) | None = None
    __properties = ['data']

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SchoolsSchoolIdDeletionsGet200Response:
        """Create an instance of SchoolsSchoolIdDeletionsGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SchoolsSchoolIdDeletionsGet200Response:
        """Create an instance of SchoolsSchoolIdDeletionsGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SchoolsSchoolIdDeletionsGet200Response.parse_obj(obj)

        _obj = SchoolsSchoolIdDeletionsGet200Response.parse_obj(
            {
                'data': [Deletion.from_dict(_item) for _item in obj.get('data')]
                if obj.get('data') is not None
                else None
            }
        )
        return _obj
