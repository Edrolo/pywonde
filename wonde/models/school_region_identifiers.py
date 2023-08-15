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
from typing import Optional

from pydantic import BaseModel, StrictInt


class SchoolRegionIdentifiers(BaseModel):
    """
    SchoolRegionIdentifiers
    """

    la_code: Optional[StrictInt] = None
    establishment_number: Optional[StrictInt] = None
    urn: Optional[StrictInt] = None
    __properties = ['la_code', 'establishment_number', 'urn']

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
    def from_json(cls, json_str: str) -> SchoolRegionIdentifiers:
        """Create an instance of SchoolRegionIdentifiers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SchoolRegionIdentifiers:
        """Create an instance of SchoolRegionIdentifiers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SchoolRegionIdentifiers.parse_obj(obj)

        _obj = SchoolRegionIdentifiers.parse_obj(
            {
                'la_code': obj.get('la_code'),
                'establishment_number': obj.get('establishment_number'),
                'urn': obj.get('urn'),
            }
        )
        return _obj
