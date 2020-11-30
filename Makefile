grpc-py:
	@python -m grpc_tools.protoc \
		-I../portal/libs/proto/src/proto/python_files \
		--python_out=./apps/files/grpc/generated \
		--grpc_python_out=./apps/files/grpc/generated \
		../portal/libs/proto/src/proto/python_files/*.proto


grpc-acts:
	@python -m grpc_tools.protoc \
		-I../portal/libs/proto/src/proto/acts \
		--python_out=./apps/files/grpc/generated \
		--grpc_python_out=./apps/files/grpc/generated \
		../portal/libs/proto/src/proto/acts/*.proto