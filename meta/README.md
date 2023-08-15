This folder contains a hand-authored OpenAPI spec for Wonde, `wonde-openapi.
yaml`, interpreted from [Wonde's API documentation](https://docs.wonde.com/docs/api/sync) 
with the assistance of ChatGPT Code Interpreter.

The spec is only partially complete

The Wonde API client library is generated with the Java-based 
[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) v6.6.0, which
includes a new generator, `python-nextgen`, which uses Pydantic models.

```
brew install openapi-generator
./generate-python-nextgen.sh

# The above script calls:
openapi-generator generate \
  --generator-name=python-nextgen \
  --config=openapi-generator-config.json \
  --input-spec=wonde.openapi.yaml \
  --output=..
```


Workflow:
- Make changes to wonde.openapi.yaml
- Regenerate client via ./generate-python-nextgen.sh
- Run `poetry run pre-commit run --all-files` to format the code with ruff and blue.
- Check for any errors from ruff. There currently seems to be a bug in the `*_api.py` files 
  where there's lines like `if isinstance(_params['updated_after'], datetime):` but `datetime`
  is not imported.
- If there are files that shouldn't be regenerated, add them to `.openapi-generator-ignore`,
  e.g. `pyproject.toml`.



Customization of templates etc:
https://github.com/OpenAPITools/openapi-generator/blob/master/docs/customization.md
