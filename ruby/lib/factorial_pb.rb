# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: factorial.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_message "FactorialRequest" do
    optional :n, :int32, 1
  end
  add_message "FactorialResponse" do
    optional :result, :int32, 1
  end
end

FactorialRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("FactorialRequest").msgclass
FactorialResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("FactorialResponse").msgclass