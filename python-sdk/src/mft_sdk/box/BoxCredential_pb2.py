# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: box/BoxCredential.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CredCommon_pb2 as CredCommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x62ox/BoxCredential.proto\x12,org.apache.airavata.mft.credential.stubs.box\x1a\x10\x43redCommon.proto\"2\n\tBoxSecret\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\"f\n\x13\x42oxSecretGetRequest\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"l\n\x16\x42oxSecretCreateRequest\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"~\n\x16\x42oxSecretUpdateRequest\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12=\n\nauthzToken\x18\x03 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"i\n\x16\x42oxSecretDeleteRequest\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthTokenB\x02P\x01\x62\x06proto3')



_BOXSECRET = DESCRIPTOR.message_types_by_name['BoxSecret']
_BOXSECRETGETREQUEST = DESCRIPTOR.message_types_by_name['BoxSecretGetRequest']
_BOXSECRETCREATEREQUEST = DESCRIPTOR.message_types_by_name['BoxSecretCreateRequest']
_BOXSECRETUPDATEREQUEST = DESCRIPTOR.message_types_by_name['BoxSecretUpdateRequest']
_BOXSECRETDELETEREQUEST = DESCRIPTOR.message_types_by_name['BoxSecretDeleteRequest']
BoxSecret = _reflection.GeneratedProtocolMessageType('BoxSecret', (_message.Message,), {
  'DESCRIPTOR' : _BOXSECRET,
  '__module__' : 'box.BoxCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.box.BoxSecret)
  })
_sym_db.RegisterMessage(BoxSecret)

BoxSecretGetRequest = _reflection.GeneratedProtocolMessageType('BoxSecretGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOXSECRETGETREQUEST,
  '__module__' : 'box.BoxCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.box.BoxSecretGetRequest)
  })
_sym_db.RegisterMessage(BoxSecretGetRequest)

BoxSecretCreateRequest = _reflection.GeneratedProtocolMessageType('BoxSecretCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOXSECRETCREATEREQUEST,
  '__module__' : 'box.BoxCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.box.BoxSecretCreateRequest)
  })
_sym_db.RegisterMessage(BoxSecretCreateRequest)

BoxSecretUpdateRequest = _reflection.GeneratedProtocolMessageType('BoxSecretUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOXSECRETUPDATEREQUEST,
  '__module__' : 'box.BoxCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.box.BoxSecretUpdateRequest)
  })
_sym_db.RegisterMessage(BoxSecretUpdateRequest)

BoxSecretDeleteRequest = _reflection.GeneratedProtocolMessageType('BoxSecretDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOXSECRETDELETEREQUEST,
  '__module__' : 'box.BoxCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.box.BoxSecretDeleteRequest)
  })
_sym_db.RegisterMessage(BoxSecretDeleteRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _BOXSECRET._serialized_start=91
  _BOXSECRET._serialized_end=141
  _BOXSECRETGETREQUEST._serialized_start=143
  _BOXSECRETGETREQUEST._serialized_end=245
  _BOXSECRETCREATEREQUEST._serialized_start=247
  _BOXSECRETCREATEREQUEST._serialized_end=355
  _BOXSECRETUPDATEREQUEST._serialized_start=357
  _BOXSECRETUPDATEREQUEST._serialized_end=483
  _BOXSECRETDELETEREQUEST._serialized_start=485
  _BOXSECRETDELETEREQUEST._serialized_end=590
# @@protoc_insertion_point(module_scope)
