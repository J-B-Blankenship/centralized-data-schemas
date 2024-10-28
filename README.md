# Instructions for Protocol Buffer

This project assumes a version of 3.28.3.

## Setup

- Navigate to https://github.com/protocolbuffers/protobuf/releases/tag/v28.3
- Install OS specific `protoc` compiler
- Add to your OS path

## Proto Generation

This section assumes the `protoc` compiler is available on your OS path. The following only includes the `pizzeria` directory and assumes no sub-directories.

- Python: `protoc --proto_path=. --python_out=./generated pizzeria/*.proto`
- C#: `protoc --proto_path=. --csharp_out=./generated pizzeria/*.proto`
- Dart: `protoc --proto_path=. --dart_out=./generated pizzeria/*.proto`

## Utilization of the Repo

This repo does not contain generated files. 
