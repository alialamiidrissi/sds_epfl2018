# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import SVM_pb2 as SVM__pb2


class SVMStub(object):
  """Interface exported by the server.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetWeights = channel.unary_unary(
        '/project.SVM/GetWeights',
        request_serializer=SVM__pb2.WeightUpdate.SerializeToString,
        response_deserializer=SVM__pb2.Row.FromString,
        )


class SVMServicer(object):
  """Interface exported by the server.

  """

  def GetWeights(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SVMServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetWeights': grpc.unary_unary_rpc_method_handler(
          servicer.GetWeights,
          request_deserializer=SVM__pb2.WeightUpdate.FromString,
          response_serializer=SVM__pb2.Row.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'project.SVM', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))