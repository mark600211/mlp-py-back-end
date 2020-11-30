# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: python_files.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='python_files.proto',
  package='python_files_service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12python_files.proto\x12\x14python_files_service\"a\n\x08TemplRes\x12\x38\n\x0bresTmplData\x18\x01 \x01(\x0b\x32!.python_files_service.ResTmplDataH\x00\x12\x0f\n\x05\x65rror\x18\x02 \x01(\tH\x00\x42\n\n\x08response\"j\n\x0bResTmplData\x12\r\n\x05\x64ocId\x18\x01 \x01(\t\x12\x0e\n\x06synUrl\x18\x02 \x01(\t\x12.\n\x05title\x18\x03 \x01(\x0e\x32\x1f.python_files_service.TitleType\x12\x0c\n\x04name\x18\x04 \x01(\t\"E\n\x08TemplReq\x12\r\n\x05\x61\x63tId\x18\x01 \x01(\t\x12*\n\x05rules\x18\x02 \x01(\x0b\x32\x1b.python_files_service.Rules\"=\n\x05Rules\x12\x0c\n\x04path\x18\x01 \x01(\t\x12&\n\x03\x63gc\x18\x02 \x01(\x0b\x32\x19.python_files_service.CGC\"\xc2\x01\n\x03\x43GC\x12\x12\n\ncustomerId\x18\x01 \x01(\t\x12\x19\n\x11generalCustomerId\x18\x02 \x01(\t\x12\x38\n\x0fprintedCustomer\x18\x03 \x01(\x0e\x32\x1f.python_files_service.PrintType\x12?\n\x16printedGeneralCustomer\x18\x04 \x01(\x0e\x32\x1f.python_files_service.PrintType\x12\x11\n\tisDefault\x18\x05 \x01(\x08\"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x15\n\x04\x46ile\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\"Y\n\x08Response\x12\x30\n\x07resData\x18\x01 \x01(\x0b\x32\x1d.python_files_service.ResDataH\x00\x12\x0f\n\x05\x65rror\x18\x02 \x01(\tH\x00\x42\n\n\x08response\"Y\n\x07Request\x12\x0f\n\x05\x63hunk\x18\x01 \x01(\x0cH\x00\x12\x32\n\x08metadata\x18\x02 \x01(\x0b\x32\x1e.python_files_service.MetadataH\x00\x42\t\n\x07request\"j\n\x08Metadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rupload_length\x18\x02 \x01(\x03\x12;\n\x0fupload_metadata\x18\x03 \x01(\x0b\x32\".python_files_service.FileMetadata\"T\n\x0c\x46ileMetadata\x12\r\n\x05\x61\x63tId\x18\x01 \x01(\t\x12\x10\n\x08\x66iletype\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x11\n\textension\x18\x04 \x01(\t\"(\n\x07ResData\x12\r\n\x05\x64ocId\x18\x01 \x01(\t\x12\x0e\n\x06synUrl\x18\x02 \x01(\t*[\n\tTitleType\x12\x16\n\x12UNKNOWN_TITLE_TYPE\x10\x00\x12\x07\n\x03\x41\x43T\x10\x01\x12\x0b\n\x07\x41\x43T_PDF\x10\x02\x12\x0c\n\x08PROTOCOL\x10\x03\x12\x12\n\x0e\x46INAL_PROTOCOL\x10\x04*\x8c\x01\n\tPrintType\x12\x16\n\x12UNKNOWN_PRINT_TYPE\x10\x00\x12\x12\n\x0eSHORT_CUSTOMER\x10\x01\x12\x11\n\rLONG_CUSTOMER\x10\x02\x12\x1a\n\x16SHORT_GENERAL_CUSTOMER\x10\x03\x12\x19\n\x15LONG_GENERAL_CUSTOMER\x10\x04\x12\t\n\x05\x45MPTY\x10\x05\x32\x88\x02\n\x12PythonFilesService\x12H\n\x0c\x44ownloadFile\x12\x1a.python_files_service.Path\x1a\x1a.python_files_service.File0\x01\x12M\n\nUploadFile\x12\x1d.python_files_service.Request\x1a\x1e.python_files_service.Response(\x01\x12Y\n\x15\x43reateDocFromTemplate\x12\x1e.python_files_service.TemplReq\x1a\x1e.python_files_service.TemplRes0\x01\x62\x06proto3'
)

_TITLETYPE = _descriptor.EnumDescriptor(
  name='TitleType',
  full_name='python_files_service.TitleType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TITLE_TYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACT_PDF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROTOCOL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FINAL_PROTOCOL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1045,
  serialized_end=1136,
)
_sym_db.RegisterEnumDescriptor(_TITLETYPE)

TitleType = enum_type_wrapper.EnumTypeWrapper(_TITLETYPE)
_PRINTTYPE = _descriptor.EnumDescriptor(
  name='PrintType',
  full_name='python_files_service.PrintType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PRINT_TYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHORT_CUSTOMER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LONG_CUSTOMER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHORT_GENERAL_CUSTOMER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LONG_GENERAL_CUSTOMER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1139,
  serialized_end=1279,
)
_sym_db.RegisterEnumDescriptor(_PRINTTYPE)

PrintType = enum_type_wrapper.EnumTypeWrapper(_PRINTTYPE)
UNKNOWN_TITLE_TYPE = 0
ACT = 1
ACT_PDF = 2
PROTOCOL = 3
FINAL_PROTOCOL = 4
UNKNOWN_PRINT_TYPE = 0
SHORT_CUSTOMER = 1
LONG_CUSTOMER = 2
SHORT_GENERAL_CUSTOMER = 3
LONG_GENERAL_CUSTOMER = 4
EMPTY = 5



_TEMPLRES = _descriptor.Descriptor(
  name='TemplRes',
  full_name='python_files_service.TemplRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resTmplData', full_name='python_files_service.TemplRes.resTmplData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='python_files_service.TemplRes.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='response', full_name='python_files_service.TemplRes.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=44,
  serialized_end=141,
)


_RESTMPLDATA = _descriptor.Descriptor(
  name='ResTmplData',
  full_name='python_files_service.ResTmplData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='python_files_service.ResTmplData.docId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='synUrl', full_name='python_files_service.ResTmplData.synUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='python_files_service.ResTmplData.title', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='python_files_service.ResTmplData.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=143,
  serialized_end=249,
)


_TEMPLREQ = _descriptor.Descriptor(
  name='TemplReq',
  full_name='python_files_service.TemplReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actId', full_name='python_files_service.TemplReq.actId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rules', full_name='python_files_service.TemplReq.rules', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=251,
  serialized_end=320,
)


_RULES = _descriptor.Descriptor(
  name='Rules',
  full_name='python_files_service.Rules',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='python_files_service.Rules.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cgc', full_name='python_files_service.Rules.cgc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=322,
  serialized_end=383,
)


_CGC = _descriptor.Descriptor(
  name='CGC',
  full_name='python_files_service.CGC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customerId', full_name='python_files_service.CGC.customerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generalCustomerId', full_name='python_files_service.CGC.generalCustomerId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='printedCustomer', full_name='python_files_service.CGC.printedCustomer', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='printedGeneralCustomer', full_name='python_files_service.CGC.printedGeneralCustomer', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isDefault', full_name='python_files_service.CGC.isDefault', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=386,
  serialized_end=580,
)


_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='python_files_service.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='python_files_service.Path.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=582,
  serialized_end=602,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='python_files_service.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='python_files_service.File.chunk', index=0,
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
  serialized_start=604,
  serialized_end=625,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='python_files_service.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resData', full_name='python_files_service.Response.resData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='python_files_service.Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='response', full_name='python_files_service.Response.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=627,
  serialized_end=716,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='python_files_service.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='python_files_service.Request.chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='python_files_service.Request.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='request', full_name='python_files_service.Request.request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=718,
  serialized_end=807,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='python_files_service.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='python_files_service.Metadata.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_length', full_name='python_files_service.Metadata.upload_length', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_metadata', full_name='python_files_service.Metadata.upload_metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=809,
  serialized_end=915,
)


_FILEMETADATA = _descriptor.Descriptor(
  name='FileMetadata',
  full_name='python_files_service.FileMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actId', full_name='python_files_service.FileMetadata.actId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filetype', full_name='python_files_service.FileMetadata.filetype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='python_files_service.FileMetadata.filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='python_files_service.FileMetadata.extension', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=917,
  serialized_end=1001,
)


_RESDATA = _descriptor.Descriptor(
  name='ResData',
  full_name='python_files_service.ResData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docId', full_name='python_files_service.ResData.docId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='synUrl', full_name='python_files_service.ResData.synUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1003,
  serialized_end=1043,
)

_TEMPLRES.fields_by_name['resTmplData'].message_type = _RESTMPLDATA
_TEMPLRES.oneofs_by_name['response'].fields.append(
  _TEMPLRES.fields_by_name['resTmplData'])
_TEMPLRES.fields_by_name['resTmplData'].containing_oneof = _TEMPLRES.oneofs_by_name['response']
_TEMPLRES.oneofs_by_name['response'].fields.append(
  _TEMPLRES.fields_by_name['error'])
_TEMPLRES.fields_by_name['error'].containing_oneof = _TEMPLRES.oneofs_by_name['response']
_RESTMPLDATA.fields_by_name['title'].enum_type = _TITLETYPE
_TEMPLREQ.fields_by_name['rules'].message_type = _RULES
_RULES.fields_by_name['cgc'].message_type = _CGC
_CGC.fields_by_name['printedCustomer'].enum_type = _PRINTTYPE
_CGC.fields_by_name['printedGeneralCustomer'].enum_type = _PRINTTYPE
_RESPONSE.fields_by_name['resData'].message_type = _RESDATA
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['resData'])
_RESPONSE.fields_by_name['resData'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['error'])
_RESPONSE.fields_by_name['error'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_REQUEST.fields_by_name['metadata'].message_type = _METADATA
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['chunk'])
_REQUEST.fields_by_name['chunk'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['metadata'])
_REQUEST.fields_by_name['metadata'].containing_oneof = _REQUEST.oneofs_by_name['request']
_METADATA.fields_by_name['upload_metadata'].message_type = _FILEMETADATA
DESCRIPTOR.message_types_by_name['TemplRes'] = _TEMPLRES
DESCRIPTOR.message_types_by_name['ResTmplData'] = _RESTMPLDATA
DESCRIPTOR.message_types_by_name['TemplReq'] = _TEMPLREQ
DESCRIPTOR.message_types_by_name['Rules'] = _RULES
DESCRIPTOR.message_types_by_name['CGC'] = _CGC
DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['FileMetadata'] = _FILEMETADATA
DESCRIPTOR.message_types_by_name['ResData'] = _RESDATA
DESCRIPTOR.enum_types_by_name['TitleType'] = _TITLETYPE
DESCRIPTOR.enum_types_by_name['PrintType'] = _PRINTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TemplRes = _reflection.GeneratedProtocolMessageType('TemplRes', (_message.Message,), {
  'DESCRIPTOR' : _TEMPLRES,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.TemplRes)
  })
_sym_db.RegisterMessage(TemplRes)

ResTmplData = _reflection.GeneratedProtocolMessageType('ResTmplData', (_message.Message,), {
  'DESCRIPTOR' : _RESTMPLDATA,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.ResTmplData)
  })
_sym_db.RegisterMessage(ResTmplData)

TemplReq = _reflection.GeneratedProtocolMessageType('TemplReq', (_message.Message,), {
  'DESCRIPTOR' : _TEMPLREQ,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.TemplReq)
  })
_sym_db.RegisterMessage(TemplReq)

Rules = _reflection.GeneratedProtocolMessageType('Rules', (_message.Message,), {
  'DESCRIPTOR' : _RULES,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.Rules)
  })
_sym_db.RegisterMessage(Rules)

CGC = _reflection.GeneratedProtocolMessageType('CGC', (_message.Message,), {
  'DESCRIPTOR' : _CGC,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.CGC)
  })
_sym_db.RegisterMessage(CGC)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.Path)
  })
_sym_db.RegisterMessage(Path)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.File)
  })
_sym_db.RegisterMessage(File)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.Response)
  })
_sym_db.RegisterMessage(Response)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.Request)
  })
_sym_db.RegisterMessage(Request)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

FileMetadata = _reflection.GeneratedProtocolMessageType('FileMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FILEMETADATA,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.FileMetadata)
  })
_sym_db.RegisterMessage(FileMetadata)

ResData = _reflection.GeneratedProtocolMessageType('ResData', (_message.Message,), {
  'DESCRIPTOR' : _RESDATA,
  '__module__' : 'python_files_pb2'
  # @@protoc_insertion_point(class_scope:python_files_service.ResData)
  })
_sym_db.RegisterMessage(ResData)



_PYTHONFILESSERVICE = _descriptor.ServiceDescriptor(
  name='PythonFilesService',
  full_name='python_files_service.PythonFilesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1282,
  serialized_end=1546,
  methods=[
  _descriptor.MethodDescriptor(
    name='DownloadFile',
    full_name='python_files_service.PythonFilesService.DownloadFile',
    index=0,
    containing_service=None,
    input_type=_PATH,
    output_type=_FILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='python_files_service.PythonFilesService.UploadFile',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateDocFromTemplate',
    full_name='python_files_service.PythonFilesService.CreateDocFromTemplate',
    index=2,
    containing_service=None,
    input_type=_TEMPLREQ,
    output_type=_TEMPLRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PYTHONFILESSERVICE)

DESCRIPTOR.services_by_name['PythonFilesService'] = _PYTHONFILESSERVICE

# @@protoc_insertion_point(module_scope)
