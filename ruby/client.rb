this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'factorial_services_pb'

def main
    stub = MathService::Stub.new('0.0.0.0:36215', :this_channel_is_insecure)
    result = stub.factorial(FactorialRequest.new(n: 3)).result
    p result
end

main
