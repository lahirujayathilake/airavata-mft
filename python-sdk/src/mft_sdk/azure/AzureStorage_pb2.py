# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/AzureStorage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61zure/AzureStorage.proto\x12\x34org.apache.airavata.mft.resource.stubs.azure.storage\"B\n\x0c\x41zureStorage\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x11\n\tcontainer\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"8\n\x17\x41zureStorageListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"p\n\x18\x41zureStorageListResponse\x12T\n\x08storages\x18\x01 \x03(\x0b\x32\x42.org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorage\"+\n\x16\x41zureStorageGetRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"O\n\x19\x41zureStorageCreateRequest\x12\x11\n\tcontainer\x18\x01 \x01(\t\x12\x11\n\tstorageId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"O\n\x19\x41zureStorageUpdateRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x11\n\tcontainer\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\".\n\x19\x41zureStorageDeleteRequest\x12\x11\n\tstorageId\x18\x01 \x01(\tB\x02P\x01\x62\x06proto3')



_AZURESTORAGE = DESCRIPTOR.message_types_by_name['AzureStorage']
_AZURESTORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['AzureStorageListRequest']
_AZURESTORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['AzureStorageListResponse']
_AZURESTORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['AzureStorageGetRequest']
_AZURESTORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['AzureStorageCreateRequest']
_AZURESTORAGEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['AzureStorageUpdateRequest']
_AZURESTORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['AzureStorageDeleteRequest']
AzureStorage = _reflection.GeneratedProtocolMessageType('AzureStorage', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGE,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorage)
  })
_sym_db.RegisterMessage(AzureStorage)

AzureStorageListRequest = _reflection.GeneratedProtocolMessageType('AzureStorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGELISTREQUEST,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorageListRequest)
  })
_sym_db.RegisterMessage(AzureStorageListRequest)

AzureStorageListResponse = _reflection.GeneratedProtocolMessageType('AzureStorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGELISTRESPONSE,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorageListResponse)
  })
_sym_db.RegisterMessage(AzureStorageListResponse)

AzureStorageGetRequest = _reflection.GeneratedProtocolMessageType('AzureStorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGEGETREQUEST,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorageGetRequest)
  })
_sym_db.RegisterMessage(AzureStorageGetRequest)

AzureStorageCreateRequest = _reflection.GeneratedProtocolMessageType('AzureStorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGECREATEREQUEST,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorageCreateRequest)
  })
_sym_db.RegisterMessage(AzureStorageCreateRequest)

AzureStorageUpdateRequest = _reflection.GeneratedProtocolMessageType('AzureStorageUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGEUPDATEREQUEST,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorageUpdateRequest)
  })
_sym_db.RegisterMessage(AzureStorageUpdateRequest)

AzureStorageDeleteRequest = _reflection.GeneratedProtocolMessageType('AzureStorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORAGEDELETEREQUEST,
  '__module__' : 'azure.AzureStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.azure.storage.AzureStorageDeleteRequest)
  })
_sym_db.RegisterMessage(AzureStorageDeleteRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _AZURESTORAGE._serialized_start=82
  _AZURESTORAGE._serialized_end=148
  _AZURESTORAGELISTREQUEST._serialized_start=150
  _AZURESTORAGELISTREQUEST._serialized_end=206
  _AZURESTORAGELISTRESPONSE._serialized_start=208
  _AZURESTORAGELISTRESPONSE._serialized_end=320
  _AZURESTORAGEGETREQUEST._serialized_start=322
  _AZURESTORAGEGETREQUEST._serialized_end=365
  _AZURESTORAGECREATEREQUEST._serialized_start=367
  _AZURESTORAGECREATEREQUEST._serialized_end=446
  _AZURESTORAGEUPDATEREQUEST._serialized_start=448
  _AZURESTORAGEUPDATEREQUEST._serialized_end=527
  _AZURESTORAGEDELETEREQUEST._serialized_start=529
  _AZURESTORAGEDELETEREQUEST._serialized_end=575
# @@protoc_insertion_point(module_scope)
