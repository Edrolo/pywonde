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

from pydantic import BaseModel, Field, StrictBool


class SchoolMeta(BaseModel):
    """
    SchoolMeta
    """

    online: StrictBool | None = Field(None, description='If the school is online')
    approved: StrictBool | None = Field(
        None, description='If the school has approved access to application'
    )
    audited: StrictBool | None = Field(
        None, description='If the school has been audited for data completeness'
    )
    custom_attendance_codes: StrictBool | None = Field(
        None, description='If the school has their own custom attendance codes'
    )
    __properties = ['online', 'approved', 'audited', 'custom_attendance_codes']

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
    def from_json(cls, json_str: str) -> SchoolMeta:
        """Create an instance of SchoolMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SchoolMeta:
        """Create an instance of SchoolMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SchoolMeta.parse_obj(obj)

        _obj = SchoolMeta.parse_obj(
            {
                'online': obj.get('online'),
                'approved': obj.get('approved'),
                'audited': obj.get('audited'),
                'custom_attendance_codes': obj.get('custom_attendance_codes'),
            }
        )
        return _obj
