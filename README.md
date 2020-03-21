#RESOURCE NODE

This resource node can save a single object and replicate the result to one more pre-defined instance

## Setup
This was built using Python, Flask and Invoke.

This project requires the following:
1. docker
2. docker-compose
3. Python 3.6

To start the project locally run the following
1. Create a virtual python env
```bash
$ virtualenv -p python3.6 venv
$ source venv/bin/activate

```
2. Setup the required python packages
```bash
$ pip install -r requirements-dev.txt -r requirements.txt
```

3. Check that everything is working
```bash
inv test
```
Which will build the docker image start the docker compose and run all tests.

## APIs
### Health Check
Path: /api/healthcheck
Method: GET

Should return 200 if the service is healthy


### Resoruce - read
Path: /api/resource
Method: GET

Returns 200 on success and the saved object if there is one.

### Resoruce - save
Path: /api/resource
Method: POST
Request Body: Any valid json you want

Returns 200 on success


## Tests
### Unit
Verify single class logic

### Integration
Tests classes which interact with external components

### Component
Runs local end to end tests
