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

from pydantic import Field, StrictInt, StrictStr, validate_arguments
from typing_extensions import Annotated

from wonde.api_client import ApiClient
from wonde.api_response import ApiResponse
from wonde.exceptions import ApiTypeError, ApiValueError  # noqa: F401
from wonde.models.list_school_subjects200_response import ListSchoolSubjects200Response
from wonde.models.subject import Subject


class SubjectsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_school_subject(
        self,
        school_id: Annotated[
            StrictStr, Field(..., description='ID of the school to retrieve the subject from')
        ],
        subject_id: Annotated[StrictStr, Field(..., description='ID of the subject to retrieve')],
        include: Annotated[
            Optional[StrictStr], Field(description='Comma separated list of objects to include.')
        ] = None,
        **kwargs
    ) -> Subject:
        """Retrieve a specific subject for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_school_subject(school_id, subject_id, include, async_req=True)
        >>> result = thread.get()

        :param school_id: ID of the school to retrieve the subject from (required)
        :type school_id: str
        :param subject_id: ID of the subject to retrieve (required)
        :type subject_id: str
        :param include: Comma separated list of objects to include.
        :type include: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Subject
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = 'Error! Please call the get_school_subject_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data'
            raise ValueError(message)
        return self.get_school_subject_with_http_info(school_id, subject_id, include, **kwargs)

    @validate_arguments
    def get_school_subject_with_http_info(
        self,
        school_id: Annotated[
            StrictStr, Field(..., description='ID of the school to retrieve the subject from')
        ],
        subject_id: Annotated[StrictStr, Field(..., description='ID of the subject to retrieve')],
        include: Annotated[
            Optional[StrictStr], Field(description='Comma separated list of objects to include.')
        ] = None,
        **kwargs
    ) -> ApiResponse:
        """Retrieve a specific subject for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_school_subject_with_http_info(school_id, subject_id, include, async_req=True)
        >>> result = thread.get()

        :param school_id: ID of the school to retrieve the subject from (required)
        :type school_id: str
        :param subject_id: ID of the subject to retrieve (required)
        :type subject_id: str
        :param include: Comma separated list of objects to include.
        :type include: str
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
        :rtype: tuple(Subject, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['school_id', 'subject_id', 'include']
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
                    "Got an unexpected keyword argument '%s'" ' to method get_school_subject' % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['school_id']:
            _path_params['school_id'] = _params['school_id']

        if _params['subject_id']:
            _path_params['subject_id'] = _params['subject_id']

        # process the query parameters
        _query_params = []
        if _params.get('include') is not None:
            _query_params.append(('include', _params['include']))

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
            '200': 'Subject',
        }

        return self.api_client.call_api(
            '/schools/{school_id}/subjects/{subject_id}',
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
    def list_school_subjects(
        self,
        school_id: Annotated[
            StrictStr, Field(..., description='ID of the school to retrieve subjects for')
        ],
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
            Optional[StrictStr], Field(description='Comma separated list of objects to include.')
        ] = None,
        subject_code: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided subject code.')
        ] = None,
        subject_name: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided subject name.')
        ] = None,
        **kwargs
    ) -> ListSchoolSubjects200Response:
        """Retrieve subjects for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_school_subjects(school_id, updated_after, updated_before, per_page, page, cursor, include, subject_code, subject_name, async_req=True)
        >>> result = thread.get()

        :param school_id: ID of the school to retrieve subjects for (required)
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
        :param include: Comma separated list of objects to include.
        :type include: str
        :param subject_code: Return results with the provided subject code.
        :type subject_code: str
        :param subject_name: Return results with the provided subject name.
        :type subject_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListSchoolSubjects200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = 'Error! Please call the list_school_subjects_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data'
            raise ValueError(message)
        return self.list_school_subjects_with_http_info(
            school_id,
            updated_after,
            updated_before,
            per_page,
            page,
            cursor,
            include,
            subject_code,
            subject_name,
            **kwargs
        )

    @validate_arguments
    def list_school_subjects_with_http_info(
        self,
        school_id: Annotated[
            StrictStr, Field(..., description='ID of the school to retrieve subjects for')
        ],
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
            Optional[StrictStr], Field(description='Comma separated list of objects to include.')
        ] = None,
        subject_code: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided subject code.')
        ] = None,
        subject_name: Annotated[
            Optional[StrictStr], Field(description='Return results with the provided subject name.')
        ] = None,
        **kwargs
    ) -> ApiResponse:
        """Retrieve subjects for a school  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_school_subjects_with_http_info(school_id, updated_after, updated_before, per_page, page, cursor, include, subject_code, subject_name, async_req=True)
        >>> result = thread.get()

        :param school_id: ID of the school to retrieve subjects for (required)
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
        :param include: Comma separated list of objects to include.
        :type include: str
        :param subject_code: Return results with the provided subject code.
        :type subject_code: str
        :param subject_name: Return results with the provided subject name.
        :type subject_name: str
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
        :rtype: tuple(ListSchoolSubjects200Response, status_code(int), headers(HTTPHeaderDict))
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
            'subject_code',
            'subject_name',
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
                    ' to method list_school_subjects' % _key
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

        if _params.get('subject_code') is not None:
            _query_params.append(('subject_code', _params['subject_code']))

        if _params.get('subject_name') is not None:
            _query_params.append(('subject_name', _params['subject_name']))

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
            '200': 'ListSchoolSubjects200Response',
        }

        return self.api_client.call_api(
            '/schools/{school_id}/subjects',
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
