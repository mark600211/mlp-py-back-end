# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import acts_pb2 as acts__pb2


class ActsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getActForTemplater = channel.unary_unary(
                '/acts_service.ActsService/getActForTemplater',
                request_serializer=acts__pb2.actId.SerializeToString,
                response_deserializer=acts__pb2.Act.FromString,
                )
        self.GetFilePath = channel.unary_unary(
                '/acts_service.ActsService/GetFilePath',
                request_serializer=acts__pb2.actId.SerializeToString,
                response_deserializer=acts__pb2.Path.FromString,
                )


class ActsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getActForTemplater(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFilePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getActForTemplater': grpc.unary_unary_rpc_method_handler(
                    servicer.getActForTemplater,
                    request_deserializer=acts__pb2.actId.FromString,
                    response_serializer=acts__pb2.Act.SerializeToString,
            ),
            'GetFilePath': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFilePath,
                    request_deserializer=acts__pb2.actId.FromString,
                    response_serializer=acts__pb2.Path.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'acts_service.ActsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ActsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getActForTemplater(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acts_service.ActsService/getActForTemplater',
            acts__pb2.actId.SerializeToString,
            acts__pb2.Act.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFilePath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/acts_service.ActsService/GetFilePath',
            acts__pb2.actId.SerializeToString,
            acts__pb2.Path.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
