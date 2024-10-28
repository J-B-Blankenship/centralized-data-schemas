# Instructions for Protocol Buffer

This project assumes a version of 3.28.3.

## Setup

- Navigate to https://github.com/protocolbuffers/protobuf/releases/tag/v28.3
- Install OS specific `protoc` compiler
- Add to your OS path
- eg. on mac:
- "sudo mv protoc /usr/local/bin/" to move the protoc file to the correct path
- Then if needing to allow "sudo xattr -rd com.apple.quarantine /usr/local/bin/protoc" (if used the above path)

## Proto Generation

This section assumes the `protoc` compiler is available on your OS path. The following only includes the `pizzeria` directory and assumes no sub-directories.

- Python: `protoc --proto_path=. --python_out=./generated pizzeria/*.proto`
- C#: `protoc --proto_path=. --csharp_out=./generated pizzeria/*.proto`
- Dart: `protoc --proto_path=. --dart_out=./generated pizzeria/*.proto`

