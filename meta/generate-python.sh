#!/usr/bin/env sh
# Generate the Python client from the OpenAPI specification,
# using the docker-based openapi-generator tool with the python generator.

#export PYTHON_POST_PROCESS_FILE="ruff"

# GENERATOR_VERSION=v6.6.0
GENERATOR_VERSION=v7.0.1

# Note: We will run the container as the current user/group, so that the generated files
#       are owned by the current user, not by root.
docker run --rm \
  --user $(id --user):$(id --group) \
  -v ${PWD}/..:/project \
  openapitools/openapi-generator-cli:${GENERATOR_VERSION} generate \
  --generator-name=python \
  --config=/project/meta/openapi-generator-config.json \
  --input-spec=/project/meta/wonde.openapi.yaml \
  --output=/project
#  --enable-post-process-file \

# poetry run pre-commit run --all-files
pre-commit run --all-files
