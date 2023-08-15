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

from pydantic import BaseModel, StrictStr, conlist

from wonde.models.acl_ids_inner import ACLIdsInner


class ACL(BaseModel):
    """
    ACL
    """

    mode: StrictStr | None = None
    ids: conlist(ACLIdsInner) | None = None
    __properties = ['mode', 'ids']

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
    def from_json(cls, json_str: str) -> ACL:
        """Create an instance of ACL from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ids (list)
        _items = []
        if self.ids:
            for _item in self.ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ids'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ACL:
        """Create an instance of ACL from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ACL.parse_obj(obj)

        _obj = ACL.parse_obj(
            {
                'mode': obj.get('mode'),
                'ids': [ACLIdsInner.from_dict(_item) for _item in obj.get('ids')]
                if obj.get('ids') is not None
                else None,
            }
        )
        return _obj