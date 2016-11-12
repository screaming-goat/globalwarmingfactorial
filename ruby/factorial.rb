#!/usr/bin/env ruby

this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'factorial_services_pb'

# FactorialServer is simple server that implements the Helloworld Greeter server.
class FactorialServer < MathService::Service
    def factorial(request, _unused_call)
        p request
        if request.n == 1
            return responder(1)
        end
        lower_sum = requester(request.n - 1)
        responder(request.n * lower_sum)
    end
end

# main starts an RpcServer that receives requests to FactorialServer at the sample
# server port.
def main
    s = GRPC::RpcServer.new
    s.add_http2_port('0.0.0.0:36215', :this_port_is_insecure)
    s.handle(FactorialServer)
    s.run_till_terminated
end


def requester (new_n)
    p "requester"
    p new_n
    stub = MathService::Stub.new('0.0.0.0:36215', :this_channel_is_insecure)
    result = stub.factorial(FactorialRequest.new(n: new_n)).result
    result
end

def responder (response)
    p "response"
    p response
    FactorialResponse.new(result: response)
end

main
