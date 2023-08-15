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

from pydantic import BaseModel, StrictInt, StrictStr

from wonde.models.school_address import SchoolAddress
from wonde.models.school_extended import SchoolExtended
from wonde.models.school_region import SchoolRegion


class School(BaseModel):
    """
    School
    """

    id: StrictStr | None = None
    name: StrictStr | None = None
    establishment_number: StrictInt | None = None
    urn: StrictInt | None = None
    phase_of_education: StrictStr | None = None
    la_code: StrictInt | None = None
    timezone: StrictStr | None = None
    mis: StrictStr | None = None
    address: SchoolAddress | None = None
    extended: SchoolExtended | None = None
    region: SchoolRegion | None = None
    __properties = [
        'id',
        'name',
        'establishment_number',
        'urn',
        'phase_of_education',
        'la_code',
        'timezone',
        'mis',
        'address',
        'extended',
        'region',
    ]

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
    def from_json(cls, json_str: str) -> School:
        """Create an instance of School from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extended
        if self.extended:
            _dict['extended'] = self.extended.to_dict()
        # override the default output from pydantic by calling `to_dict()` of region
        if self.region:
            _dict['region'] = self.region.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> School:
        """Create an instance of School from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return School.parse_obj(obj)

        _obj = School.parse_obj(
            {
                'id': obj.get('id'),
                'name': obj.get('name'),
                'establishment_number': obj.get('establishment_number'),
                'urn': obj.get('urn'),
                'phase_of_education': obj.get('phase_of_education'),
                'la_code': obj.get('la_code'),
                'timezone': obj.get('timezone'),
                'mis': obj.get('mis'),
                'address': SchoolAddress.from_dict(obj.get('address'))
                if obj.get('address') is not None
                else None,
                'extended': SchoolExtended.from_dict(obj.get('extended'))
                if obj.get('extended') is not None
                else None,
                'region': SchoolRegion.from_dict(obj.get('region'))
                if obj.get('region') is not None
                else None,
            }
        )
        return _obj