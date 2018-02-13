# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import google.cloud.oslogin_v1.proto.common_pb2 as google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2
import google.cloud.oslogin_v1.proto.oslogin_pb2 as google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2


class OsLoginServiceStub(object):
  """Cloud OS Login API

  The Cloud OS Login API allows you to manage users and their associated SSH
  public keys for logging into virtual machines on Google Cloud Platform.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DeletePosixAccount = channel.unary_unary(
        '/google.cloud.oslogin.v1.OsLoginService/DeletePosixAccount',
        request_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.DeletePosixAccountRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteSshPublicKey = channel.unary_unary(
        '/google.cloud.oslogin.v1.OsLoginService/DeleteSshPublicKey',
        request_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.DeleteSshPublicKeyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetLoginProfile = channel.unary_unary(
        '/google.cloud.oslogin.v1.OsLoginService/GetLoginProfile',
        request_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.GetLoginProfileRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.LoginProfile.FromString,
        )
    self.GetSshPublicKey = channel.unary_unary(
        '/google.cloud.oslogin.v1.OsLoginService/GetSshPublicKey',
        request_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.GetSshPublicKeyRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2.SshPublicKey.FromString,
        )
    self.ImportSshPublicKey = channel.unary_unary(
        '/google.cloud.oslogin.v1.OsLoginService/ImportSshPublicKey',
        request_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.ImportSshPublicKeyRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.ImportSshPublicKeyResponse.FromString,
        )
    self.UpdateSshPublicKey = channel.unary_unary(
        '/google.cloud.oslogin.v1.OsLoginService/UpdateSshPublicKey',
        request_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.UpdateSshPublicKeyRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2.SshPublicKey.FromString,
        )


class OsLoginServiceServicer(object):
  """Cloud OS Login API

  The Cloud OS Login API allows you to manage users and their associated SSH
  public keys for logging into virtual machines on Google Cloud Platform.
  """

  def DeletePosixAccount(self, request, context):
    """Deletes a POSIX account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSshPublicKey(self, request, context):
    """Deletes an SSH public key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLoginProfile(self, request, context):
    """Retrieves the profile information used for logging in to a virtual machine
    on Google Compute Engine.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSshPublicKey(self, request, context):
    """Retrieves an SSH public key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ImportSshPublicKey(self, request, context):
    """Adds an SSH public key and returns the profile information. Default POSIX
    account information is set when no username and UID exist as part of the
    login profile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSshPublicKey(self, request, context):
    """Updates an SSH public key and returns the profile information. This method
    supports patch semantics.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OsLoginServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DeletePosixAccount': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePosixAccount,
          request_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.DeletePosixAccountRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteSshPublicKey': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSshPublicKey,
          request_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.DeleteSshPublicKeyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetLoginProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GetLoginProfile,
          request_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.GetLoginProfileRequest.FromString,
          response_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.LoginProfile.SerializeToString,
      ),
      'GetSshPublicKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetSshPublicKey,
          request_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.GetSshPublicKeyRequest.FromString,
          response_serializer=google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2.SshPublicKey.SerializeToString,
      ),
      'ImportSshPublicKey': grpc.unary_unary_rpc_method_handler(
          servicer.ImportSshPublicKey,
          request_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.ImportSshPublicKeyRequest.FromString,
          response_serializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.ImportSshPublicKeyResponse.SerializeToString,
      ),
      'UpdateSshPublicKey': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSshPublicKey,
          request_deserializer=google_dot_cloud_dot_oslogin__v1_dot_proto_dot_oslogin__pb2.UpdateSshPublicKeyRequest.FromString,
          response_serializer=google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2.SshPublicKey.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.oslogin.v1.OsLoginService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
