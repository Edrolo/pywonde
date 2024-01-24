"""
Wonde API

API Docs

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import re  # noqa: F401
from datetime import date
from typing import Optional

from pydantic import (
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    conlist,
    validate_arguments,
)
from typing_extensions import Annotated

from wonde.api_client import ApiClient
from wonde.api_response import ApiResponse
from wonde.exceptions import ApiTypeError, ApiValueError  # noqa: F401
from wonde.models.get_school_class200_response import GetSchoolClass200Response
from wonde.models.list_school_classes200_response import ListSchoolClasses200Response


class ClassesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_school_class(
        self,
        school_id: Annotated[StrictStr, Field(..., description='The ID of the school')],
        class_id: Annotated[StrictStr, Field(..., description='The ID of the class')],
        include: Annotated[
            Optional[conlist(StrictStr)],
            Field(description='Comma separated list of objects to include'),
        ] = None,
        **kwargs
    ) -> GetSchoolClass200Response:
        """Get specific class for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_school_class(school_id, class_id, include, async_req=True)
        >>> result = thread.get()

        :param school_id: The ID of the school (required)
        :type school_id: str
        :param class_id: The ID of the class (required)
        :type class_id: str
        :param include: Comma separated list of objects to include
        :type include: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetSchoolClass200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = 'Error! Please call the get_school_class_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data'
            raise ValueError(message)
        return self.get_school_class_with_http_info(school_id, class_id, include, **kwargs)

    @validate_arguments
    def get_school_class_with_http_info(
        self,
        school_id: Annotated[StrictStr, Field(..., description='The ID of the school')],
        class_id: Annotated[StrictStr, Field(..., description='The ID of the class')],
        include: Annotated[
            Optional[conlist(StrictStr)],
            Field(description='Comma separated list of objects to include'),
        ] = None,
        **kwargs
    ) -> ApiResponse:
        """Get specific class for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_school_class_with_http_info(school_id, class_id, include, async_req=True)
        >>> result = thread.get()

        :param school_id: The ID of the school (required)
        :type school_id: str
        :param class_id: The ID of the class (required)
        :type class_id: str
        :param include: Comma separated list of objects to include
        :type include: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetSchoolClass200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['school_id', 'class_id', 'include']
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" ' to method get_school_class' % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['school_id']:
            _path_params['school_id'] = _params['school_id']

        if _params['class_id']:
            _path_params['class_id'] = _params['class_id']

        # process the query parameters
        _query_params = []
        if _params.get('include') is not None:
            _query_params.append(('include', _params['include']))
            _collection_formats['include'] = 'csv'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings = ['BasicAuth', 'BearerAuth']

        _response_types_map = {
            '200': 'GetSchoolClass200Response',
        }

        return self.api_client.call_api(
            '/schools/{school_id}/classes/{class_id}',
            'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'),
        )

    @validate_arguments
    def list_school_classes(
        self,
        school_id: Annotated[StrictStr, Field(..., description='The ID of the school')],
        updated_after: Annotated[
            Optional[date], Field(description='Return rows modified after date')
        ] = None,
        updated_before: Annotated[
            Optional[date], Field(description='Return rows modified before date')
        ] = None,
        per_page: Annotated[
            Optional[StrictInt], Field(description='Amount of rows to return')
        ] = None,
        page: Annotated[
            Optional[StrictInt], Field(description='Page offset for offset-paginated results.')
        ] = None,
        cursor: Annotated[
            Optional[StrictStr], Field(description='Page cursor for cursor-paginated results.')
        ] = None,
        include: Annotated[
            Optional[StrictStr], Field(description='Comma separated list of objects to include')
        ] = None,
        has_students: Annotated[
            Optional[StrictBool], Field(description='Only get classes that have students')
        ] = None,
        has_lessons: Annotated[
            Optional[StrictBool], Field(description='Only get classes that have lessons')
        ] = None,
        class_name: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided class name')
        ] = None,
        class_subject: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided subject id')
        ] = None,
        **kwargs
    ) -> ListSchoolClasses200Response:
        """Get all classes for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_school_classes(school_id, updated_after, updated_before, per_page, page, cursor, include, has_students, has_lessons, class_name, class_subject, async_req=True)
        >>> result = thread.get()

        :param school_id: The ID of the school (required)
        :type school_id: str
        :param updated_after: Return rows modified after date
        :type updated_after: date
        :param updated_before: Return rows modified before date
        :type updated_before: date
        :param per_page: Amount of rows to return
        :type per_page: int
        :param page: Page offset for offset-paginated results.
        :type page: int
        :param cursor: Page cursor for cursor-paginated results.
        :type cursor: str
        :param include: Comma separated list of objects to include
        :type include: str
        :param has_students: Only get classes that have students
        :type has_students: bool
        :param has_lessons: Only get classes that have lessons
        :type has_lessons: bool
        :param class_name: Return results with the provided class name
        :type class_name: str
        :param class_subject: Return results with the provided subject id
        :type class_subject: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListSchoolClasses200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = 'Error! Please call the list_school_classes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data'
            raise ValueError(message)
        return self.list_school_classes_with_http_info(
            school_id,
            updated_after,
            updated_before,
            per_page,
            page,
            cursor,
            include,
            has_students,
            has_lessons,
            class_name,
            class_subject,
            **kwargs
        )

    @validate_arguments
    def list_school_classes_with_http_info(
        self,
        school_id: Annotated[StrictStr, Field(..., description='The ID of the school')],
        updated_after: Annotated[
            Optional[date], Field(description='Return rows modified after date')
        ] = None,
        updated_before: Annotated[
            Optional[date], Field(description='Return rows modified before date')
        ] = None,
        per_page: Annotated[
            Optional[StrictInt], Field(description='Amount of rows to return')
        ] = None,
        page: Annotated[
            Optional[StrictInt], Field(description='Page offset for offset-paginated results.')
        ] = None,
        cursor: Annotated[
            Optional[StrictStr], Field(description='Page cursor for cursor-paginated results.')
        ] = None,
        include: Annotated[
            Optional[StrictStr], Field(description='Comma separated list of objects to include')
        ] = None,
        has_students: Annotated[
            Optional[StrictBool], Field(description='Only get classes that have students')
        ] = None,
        has_lessons: Annotated[
            Optional[StrictBool], Field(description='Only get classes that have lessons')
        ] = None,
        class_name: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided class name')
        ] = None,
        class_subject: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided subject id')
        ] = None,
        **kwargs
    ) -> ApiResponse:
        """Get all classes for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_school_classes_with_http_info(school_id, updated_after, updated_before, per_page, page, cursor, include, has_students, has_lessons, class_name, class_subject, async_req=True)
        >>> result = thread.get()

        :param school_id: The ID of the school (required)
        :type school_id: str
        :param updated_after: Return rows modified after date
        :type updated_after: date
        :param updated_before: Return rows modified before date
        :type updated_before: date
        :param per_page: Amount of rows to return
        :type per_page: int
        :param page: Page offset for offset-paginated results.
        :type page: int
        :param cursor: Page cursor for cursor-paginated results.
        :type cursor: str
        :param include: Comma separated list of objects to include
        :type include: str
        :param has_students: Only get classes that have students
        :type has_students: bool
        :param has_lessons: Only get classes that have lessons
        :type has_lessons: bool
        :param class_name: Return results with the provided class name
        :type class_name: str
        :param class_subject: Return results with the provided subject id
        :type class_subject: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListSchoolClasses200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'school_id',
            'updated_after',
            'updated_before',
            'per_page',
            'page',
            'cursor',
            'include',
            'has_students',
            'has_lessons',
            'class_name',
            'class_subject',
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method list_school_classes' % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['school_id']:
            _path_params['school_id'] = _params['school_id']

        # process the query parameters
        _query_params = []
        if _params.get('updated_after') is not None:
            if isinstance(_params['updated_after'], date):
                _query_params.append(
                    (
                        'updated_after',
                        _params['updated_after'].strftime(
                            self.api_client.configuration.date_format
                        ),
                    )
                )
            else:
                _query_params.append(('updated_after', _params['updated_after']))

        if _params.get('updated_before') is not None:
            if isinstance(_params['updated_before'], date):
                _query_params.append(
                    (
                        'updated_before',
                        _params['updated_before'].strftime(
                            self.api_client.configuration.date_format
                        ),
                    )
                )
            else:
                _query_params.append(('updated_before', _params['updated_before']))

        if _params.get('per_page') is not None:
            _query_params.append(('per_page', _params['per_page']))

        if _params.get('page') is not None:
            _query_params.append(('page', _params['page']))

        if _params.get('cursor') is not None:
            _query_params.append(('cursor', _params['cursor']))

        if _params.get('include') is not None:
            _query_params.append(('include', _params['include']))

        if _params.get('has_students') is not None:
            _query_params.append(('has_students', _params['has_students']))

        if _params.get('has_lessons') is not None:
            _query_params.append(('has_lessons', _params['has_lessons']))

        if _params.get('class_name') is not None:
            _query_params.append(('class_name', _params['class_name']))

        if _params.get('class_subject') is not None:
            _query_params.append(('class_subject', _params['class_subject']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings = ['BasicAuth', 'BearerAuth']

        _response_types_map = {
            '200': 'ListSchoolClasses200Response',
        }

        return self.api_client.call_api(
            '/schools/{school_id}/classes',
            'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'),
        )
