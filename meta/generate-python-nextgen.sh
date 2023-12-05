#!/usr/bin/env sh
# Generate the Python client from the OpenAPI specification,
# using the Java-based openapi-generator tool with the python-nextgen generator.

#export PYTHON_POST_PROCESS_FILE="ruff"

# openapi-generator generate \
#   --generator-name=python-nextgen \
#   --config=openapi-generator-config.json \
#   --input-spec=wonde.openapi.yaml \
#   --output=..
# #  --enable-post-process-file \

docker run --rm \
  -v ${PWD}/..:/project \
  openapitools/openapi-generator-cli generate \
  --generator-name=python \
  --config=/project/meta/openapi-generator-config.json \
  --input-spec=/project/meta/wonde.openapi.yaml \
  --output=/project
#  --enable-post-process-file \

poetry run pre-commit run --all-files
