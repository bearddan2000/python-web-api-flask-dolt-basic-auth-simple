# python-web-api-flask-dolt-basic-auth-simple

## Description
Creates an api of `dog` for a flask project.
Has the ability to query by parameters.
If path is not found, will default to 404 error.
Uses basic authentication.

| username | password |
----------------------
| user | pass |

## Tech stack
- python
- flask

## Docker stack
- python:latest
- dolthub/dolt-sql-serverdb:latest

## To run
`sudo ./install.sh -u`
- Endpoint
  - `curl -i localhost/dog -u user:pass`

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
- https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-dolt-with-flask-sqlalchemy
- [Basic auth setup](https://medium.com/tek-society/how-to-secure-your-python-flask-routes-with-basic-auth-in-5-minutes-6e3cea1448a4)
