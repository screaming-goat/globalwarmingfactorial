# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: factorial.proto for package ''

require 'grpc'
require 'factorial_pb'

module MathService
  class Service

    include GRPC::GenericService

    self.marshal_class_method = :encode
    self.unmarshal_class_method = :decode
    self.service_name = 'MathService'

    rpc :Factorial, FactorialRequest, FactorialResponse
  end

  Stub = Service.rpc_stub_class
end
