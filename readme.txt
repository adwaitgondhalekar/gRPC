command to generate grpc files from .proto file
python3 -m grpc_tools.protoc --proto_path=./ --grpc_python_out=./ ./multiply.proto