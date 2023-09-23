# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import multiply_pb2 as multiply__pb2


class MultiplierStub(object):
    """name of the service created
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.multiply = channel.unary_unary(
                '/Multiplier/multiply',
                request_serializer=multiply__pb2.clientinput.SerializeToString,
                response_deserializer=multiply__pb2.multipliedoutput.FromString,
                )


class MultiplierServicer(object):
    """name of the service created
    """

    def multiply(self, request, context):
        """name of the remote procedure
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MultiplierServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.multiply,
                    request_deserializer=multiply__pb2.clientinput.FromString,
                    response_serializer=multiply__pb2.multipliedoutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Multiplier', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Multiplier(object):
    """name of the service created
    """

    @staticmethod
    def multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Multiplier/multiply',
            multiply__pb2.clientinput.SerializeToString,
            multiply__pb2.multipliedoutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
