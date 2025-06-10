# API Testing with Schemathesis

This repository contains a helper script to run automated tests for every
endpoint defined in an OpenAPI/Swagger specification.

The approach relies on the open source tool **[Schemathesis](https://github.com/schemathesis/schemathesis)**
which generates test cases from your API specification and sends them to the
running server.

## Requirements

- Python 3.8+
- `schemathesis` installed (`pip install schemathesis`)

## Usage

1. Start your API server locally or have a reachable base URL.
2. Run the helper script with the path to your Swagger file and the API's base URL:

```bash
python run_schemathesis.py path/to/swagger.yaml http://localhost:8000
```

Schemathesis will automatically generate tests for all endpoints and report any
failures it encounters.
