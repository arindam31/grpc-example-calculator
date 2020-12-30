# This project is to show how to use GRPC with Python
### Goal is to serve functions of a calculator using gRPC.

## Basic Steps

- Create a calculator.py with some demo functions
- Write a proto file for each function.
- Create python files from proto file.  
- Write a server and a client.
- Run server, the client to test responses.

### How to run:

1. Server: `python server.py`
2. On another tab: `python client.py`

### To create python files from proto file:

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto`
