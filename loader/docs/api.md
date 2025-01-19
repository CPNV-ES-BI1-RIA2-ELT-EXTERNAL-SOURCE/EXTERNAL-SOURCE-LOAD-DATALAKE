# Connecting to the API

## Using curl (Command Line)

You can send a POST HTTP request with curl to connect to the API and send data to the `/load` endpoint.

## Example of POST /load request

Here is an example of a curl command to send a POST request with a JSON body to the FastAPI server:

```bash
curl -X POST "http://127.0.0.1:8000/load" -H "Content-Type: application/json" -d '{"key": "value"}'
```
In this example:

- X POST: Specifies that the HTTP method is POST.
- "http://127.0.0.1:8000/load": The URL of the API to which you are sending the request.
- H "Content-Type: application/json": Specifies that the request body is in JSON format.
- d '{"key": "value"}': The JSON data sent in the request body.
