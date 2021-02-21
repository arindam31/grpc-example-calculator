# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import calculator_pb2 as proto_dot_calculator__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Multiplier = channel.unary_unary(
                '/Calculator/Multiplier',
                request_serializer=proto_dot_calculator__pb2.NumList.SerializeToString,
                response_deserializer=proto_dot_calculator__pb2.Number.FromString,
                )
        self.Square = channel.unary_unary(
                '/Calculator/Square',
                request_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
                response_deserializer=proto_dot_calculator__pb2.Number.FromString,
                )
        self.SquareRoot = channel.unary_unary(
                '/Calculator/SquareRoot',
                request_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
                response_deserializer=proto_dot_calculator__pb2.Float.FromString,
                )
        self.CountLists = channel.unary_unary(
                '/Calculator/CountLists',
                request_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
                response_deserializer=proto_dot_calculator__pb2.Float.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Multiplier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Square(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SquareRoot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountLists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Multiplier': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiplier,
                    request_deserializer=proto_dot_calculator__pb2.NumList.FromString,
                    response_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
            ),
            'Square': grpc.unary_unary_rpc_method_handler(
                    servicer.Square,
                    request_deserializer=proto_dot_calculator__pb2.Number.FromString,
                    response_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
            ),
            'SquareRoot': grpc.unary_unary_rpc_method_handler(
                    servicer.SquareRoot,
                    request_deserializer=proto_dot_calculator__pb2.Number.FromString,
                    response_serializer=proto_dot_calculator__pb2.Float.SerializeToString,
            ),
            'CountLists': grpc.unary_unary_rpc_method_handler(
                    servicer.CountLists,
                    request_deserializer=proto_dot_calculator__pb2.Number.FromString,
                    response_serializer=proto_dot_calculator__pb2.Float.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Multiplier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Multiplier',
            proto_dot_calculator__pb2.NumList.SerializeToString,
            proto_dot_calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Square(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Square',
            proto_dot_calculator__pb2.Number.SerializeToString,
            proto_dot_calculator__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SquareRoot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/SquareRoot',
            proto_dot_calculator__pb2.Number.SerializeToString,
            proto_dot_calculator__pb2.Float.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CountLists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/CountLists',
            proto_dot_calculator__pb2.Number.SerializeToString,
            proto_dot_calculator__pb2.Float.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)