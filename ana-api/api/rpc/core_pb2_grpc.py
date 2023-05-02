# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api.rpc.core_pb2 as core__pb2


class ModelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.completePrompt = channel.unary_unary(
                '/core.Model/completePrompt',
                request_serializer=core__pb2.Prompt.SerializeToString,
                response_deserializer=core__pb2.PromptCompletion.FromString,
                )


class ModelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def completePrompt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'completePrompt': grpc.unary_unary_rpc_method_handler(
                    servicer.completePrompt,
                    request_deserializer=core__pb2.Prompt.FromString,
                    response_serializer=core__pb2.PromptCompletion.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'core.Model', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Model(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def completePrompt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.Model/completePrompt',
            core__pb2.Prompt.SerializeToString,
            core__pb2.PromptCompletion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
