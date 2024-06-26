"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

from pydantic import BaseModel, StrictStr, conlist, validator

from wonde.models.pagination import Pagination


class ListSchoolLessons200ResponseMeta(BaseModel):
    """
    ListSchoolLessons200ResponseMeta
    """

    pagination: Optional[Pagination] = None
    includes: Optional[conlist(StrictStr)] = None
    __properties = ['pagination', 'includes']

    @validator('includes')
    def includes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('class', 'employee', 'period', 'room'):
                raise ValueError(
                    "each list item must be one of ('class', 'employee', 'period', 'room')"
                )
        return value

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
    def from_json(cls, json_str: str) -> ListSchoolLessons200ResponseMeta:
        """Create an instance of ListSchoolLessons200ResponseMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListSchoolLessons200ResponseMeta:
        """Create an instance of ListSchoolLessons200ResponseMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListSchoolLessons200ResponseMeta.parse_obj(obj)

        _obj = ListSchoolLessons200ResponseMeta.parse_obj(
            {
                'pagination': Pagination.from_dict(obj.get('pagination'))
                if obj.get('pagination') is not None
                else None,
                'includes': obj.get('includes'),
            }
        )
        return _obj
