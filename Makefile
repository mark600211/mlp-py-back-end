grpc-gen:
	@python -m grpc_tools.protoc \
		-I../ts-back-end/libs/proto/src/proto/python_files \
		--python_out=./apps/files/grpc/generated \
		--grpc_python_out=./apps/files/grpc/generated \
		../ts-back-end/libs/proto/src/proto/python_files/*.proto
	# @sed -i -E 's/^import.*_pb2/from . \0/' ./apps/files/generated/*.py