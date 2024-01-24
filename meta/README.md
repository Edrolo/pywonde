# Readme

This folder contains a hand-authored OpenAPI spec for Wonde, `wonde-openapi.yaml`, interpreted from [Wonde's API documentation](https://docs.wonde.com/docs/api/sync) with the assistance of ChatGPT Code Interpreter.

The spec is only partially complete.

The Wonde API client library is generated with the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) via it's docker image, [openapitools/openapi-generator-cli](https://hub.docker.com/r/openapitools/openapi-generator-cli).

We currently use `v7.0.1` of the tool, which includes a now-stable `python` generator, which uses Pydantic models. This version (`v7.0.1`) was chosen as the most-recent version that is compatible with the Edrolo projects in which this client is internally used.

Use therefore assumes a working installation of docker.

## Workflow

- Make changes to `wonde.openapi.yaml`
- Regenerate client via `./generate-python.sh`
- Run `pre-commit run --all-files` to format the code with ruff and blue.
- Check for any errors from ruff. There currently seems to be a bug in the `*_api.py` files 
  where there's lines like `if isinstance(_params['updated_after'], datetime):` but `datetime`
  is not imported.
- If there are files that shouldn't be regenerated, add them to `.openapi-generator-ignore`,
  e.g. `pyproject.toml`.
- Run tests via `pytest` and fix any errors.

# References

- OpenAPI Generator: [OpenAPITools/openapi-generator: OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3)](https://github.com/OpenAPITools/openapi-generator)
- Customization of templates etc: [openapi-generator/docs/customization.md at master · OpenAPITools/openapi-generator](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/customization.md)
- Docker Image: [openapitools/openapi-generator-cli - Docker Image | Docker Hub](https://hub.docker.com/r/openapitools/openapi-generator-cli)
