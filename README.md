# stactools-hfrnet

[![PyPI](https://img.shields.io/pypi/v/stactools-hfrnet?style=for-the-badge)](https://pypi.org/project/stactools-hfrnet/)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/stactools-packages/hfrnet/continuous-integration.yml?style=for-the-badge)

- Name: hfrnet
- Package: `stactools.hfrnet`
- [stactools-hfrnet on PyPI](https://pypi.org/project/stactools-hfrnet/)
- Owner: @githubusername
- [Dataset homepage](http://example.com)
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
- Extra fields:
  - `hfrnet:custom`: A custom attribute
- [Browse the example in human-readable form](https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/stactools-packages/hfrnet/main/examples/collection.json)
- [Browse a notebook demonstrating the example item and collection](https://github.com/stactools-packages/hfrnet/tree/main/docs/example.ipynb)

A short description of the package and its usage.

## STAC examples

- [Collection](examples/collection.json)
- [Item](examples/item/item.json)

## Installation

```shell
pip install stactools-hfrnet
```

## Command-line usage

Description of the command line functions

```shell
stac hfrnet create-item source destination
```

Use `stac hfrnet --help` to see all subcommands and options.

## Contributing

We use [pre-commit](https://pre-commit.com/) to check any changes.
To set up your development environment:

```shell
uv sync
uv run pre-commit install
```

To check all files:

```shell
uv run pre-commit run --all-files
```

To run the tests:

```shell
uv run pytest -vv
```

If you've updated the STAC metadata output, update the examples:

```shell
uv run scripts/update-examples
```
