from concurrent import futures
import time

import grpc

import factorial_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MathService(factorial_pb2.MathServiceServicer):

  def Factorial(self, request, context):
    requestedN = request.n
    response = 1

    if(requestedN > 1):
        channel = grpc.insecure_channel('python-factorial:36215')
        stub = factorial_pb2.MathServiceStub(channel)
        rpcResponse = stub.Factorial(factorial_pb2.FactorialRequest(n=requestedN - 1))
        response = requestedN * rpcResponse.result

    return factorial_pb2.FactorialResponse(result=response)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  factorial_pb2.add_MathServiceServicer_to_server(MathService(), server)
  server.add_insecure_port('[::]:36215')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
