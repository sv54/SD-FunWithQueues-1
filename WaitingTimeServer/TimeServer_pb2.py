# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TimeServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TimeServer.proto',
  package='com.WaitingTimeServer.grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10TimeServer.proto\x12\x1a\x63om.WaitingTimeServer.grpc\"#\n\x14\x45stimatedTimeRequest\x12\x0b\n\x03num\x18\x01 \x01(\x05\"\x1d\n\x0cTimeResponse\x12\r\n\x05times\x18\x01 \x01(\x0c\x32s\n\rCalculateTime\x12\x62\n\x04Time\x12\x30.com.WaitingTimeServer.grpc.EstimatedTimeRequest\x1a(.com.WaitingTimeServer.grpc.TimeResponseb\x06proto3'
)




_ESTIMATEDTIMEREQUEST = _descriptor.Descriptor(
  name='EstimatedTimeRequest',
  full_name='com.WaitingTimeServer.grpc.EstimatedTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='com.WaitingTimeServer.grpc.EstimatedTimeRequest.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=83,
)


_TIMERESPONSE = _descriptor.Descriptor(
  name='TimeResponse',
  full_name='com.WaitingTimeServer.grpc.TimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='times', full_name='com.WaitingTimeServer.grpc.TimeResponse.times', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['EstimatedTimeRequest'] = _ESTIMATEDTIMEREQUEST
DESCRIPTOR.message_types_by_name['TimeResponse'] = _TIMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstimatedTimeRequest = _reflection.GeneratedProtocolMessageType('EstimatedTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ESTIMATEDTIMEREQUEST,
  '__module__' : 'TimeServer_pb2'
  # @@protoc_insertion_point(class_scope:com.WaitingTimeServer.grpc.EstimatedTimeRequest)
  })
_sym_db.RegisterMessage(EstimatedTimeRequest)

TimeResponse = _reflection.GeneratedProtocolMessageType('TimeResponse', (_message.Message,), {
  'DESCRIPTOR' : _TIMERESPONSE,
  '__module__' : 'TimeServer_pb2'
  # @@protoc_insertion_point(class_scope:com.WaitingTimeServer.grpc.TimeResponse)
  })
_sym_db.RegisterMessage(TimeResponse)



_CALCULATETIME = _descriptor.ServiceDescriptor(
  name='CalculateTime',
  full_name='com.WaitingTimeServer.grpc.CalculateTime',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=116,
  serialized_end=231,
  methods=[
  _descriptor.MethodDescriptor(
    name='Time',
    full_name='com.WaitingTimeServer.grpc.CalculateTime.Time',
    index=0,
    containing_service=None,
    input_type=_ESTIMATEDTIMEREQUEST,
    output_type=_TIMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATETIME)

DESCRIPTOR.services_by_name['CalculateTime'] = _CALCULATETIME

# @@protoc_insertion_point(module_scope)