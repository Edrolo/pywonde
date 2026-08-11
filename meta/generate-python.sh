#!/usr/bin/env sh
# Generate the Python client from the OpenAPI specification,
# using the docker-based openapi-generator tool with the python generator.

#export PYTHON_POST_PROCESS_FILE="ruff"

# v7.1.0 is the floor: it is where the `python` generator moved to pydantic v2.
# Below that the generator emits `validate_arguments` / `Field(const=True)`,
# which pydantic v2 rejects — previously worked around by hand-patching the
# generated output (commit 3ce2d7c), which any regeneration silently reverted.
GENERATOR_VERSION=v7.24.0

# Note: We will run the container as the current user/group, so that the generated files
#       are owned by the current user, not by root.
# Note: `id -u` / `id -g` are POSIX. The long forms (--user/--group) are GNU
#       coreutils only and fail on macOS's BSD id.
docker run --rm \
  --user $(id -u):$(id -g) \
  -v ${PWD}/..:/project \
  openapitools/openapi-generator-cli:${GENERATOR_VERSION} generate \
  --generator-name=python \
  --config=/project/meta/openapi-generator-config.json \
  --input-spec=/project/meta/wonde.openapi.yaml \
  --output=/project
#  --enable-post-process-file \

# Run via uvx so this works without pre-commit installed on PATH.
uvx pre-commit run --all-files
