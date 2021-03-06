# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: factorial.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='factorial.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x66\x61\x63torial.proto\"\x1d\n\x10\x46\x61\x63torialRequest\x12\t\n\x01n\x18\x01 \x01(\x04\"#\n\x11\x46\x61\x63torialResponse\x12\x0e\n\x06result\x18\x01 \x01(\x04\x32\x43\n\x0bMathService\x12\x34\n\tFactorial\x12\x11.FactorialRequest\x1a\x12.FactorialResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FACTORIALREQUEST = _descriptor.Descriptor(
  name='FactorialRequest',
  full_name='FactorialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='FactorialRequest.n', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=48,
)


_FACTORIALRESPONSE = _descriptor.Descriptor(
  name='FactorialResponse',
  full_name='FactorialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='FactorialResponse.result', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['FactorialRequest'] = _FACTORIALREQUEST
DESCRIPTOR.message_types_by_name['FactorialResponse'] = _FACTORIALRESPONSE

FactorialRequest = _reflection.GeneratedProtocolMessageType('FactorialRequest', (_message.Message,), dict(
  DESCRIPTOR = _FACTORIALREQUEST,
  __module__ = 'factorial_pb2'
  # @@protoc_insertion_point(class_scope:FactorialRequest)
  ))
_sym_db.RegisterMessage(FactorialRequest)

FactorialResponse = _reflection.GeneratedProtocolMessageType('FactorialResponse', (_message.Message,), dict(
  DESCRIPTOR = _FACTORIALRESPONSE,
  __module__ = 'factorial_pb2'
  # @@protoc_insertion_point(class_scope:FactorialResponse)
  ))
_sym_db.RegisterMessage(FactorialResponse)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class MathServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Factorial = channel.unary_unary(
        '/MathService/Factorial',
        request_serializer=FactorialRequest.SerializeToString,
        response_deserializer=FactorialResponse.FromString,
        )


class MathServiceServicer(object):

  def Factorial(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MathServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Factorial': grpc.unary_unary_rpc_method_handler(
          servicer.Factorial,
          request_deserializer=FactorialRequest.FromString,
          response_serializer=FactorialResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MathService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaMathServiceServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def Factorial(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaMathServiceStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def Factorial(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Factorial.future = None


def beta_create_MathService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('MathService', 'Factorial'): FactorialRequest.FromString,
  }
  response_serializers = {
    ('MathService', 'Factorial'): FactorialResponse.SerializeToString,
  }
  method_implementations = {
    ('MathService', 'Factorial'): face_utilities.unary_unary_inline(servicer.Factorial),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_MathService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('MathService', 'Factorial'): FactorialRequest.SerializeToString,
  }
  response_deserializers = {
    ('MathService', 'Factorial'): FactorialResponse.FromString,
  }
  cardinalities = {
    'Factorial': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'MathService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
