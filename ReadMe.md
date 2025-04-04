# Project name

### Repository description

[//]: # (TODO complete this section)

The stack is python, using flask.
It uses Make and Docker for the configuration and run.

### Setup

``` bash
make setup-python-env
make install
```

Note: if the dependencies versions are not frozen, you can use:

```bash
make freeze
```

## Run the app

### With Docker

This command requires Docker desktop app and docker-compose cli to be installed.

``` bash
make docker
```

### Locally

#### Run

``` bash
make run-locally
```

## Quality

Best practices for tests: test files must be named `test_*.py` and be located in the folder `test`.

Commands:

``` bash
# run tests
make tests

# run linter
make lint

# run pre-commit hook
make pre-commit
```
