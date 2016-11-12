from __future__ import print_function

import grpc

import sys

import factorial_pb2

import time

def run():
  requestedN = int(sys.argv[1])

  channel = grpc.insecure_channel('localhost:36215')
  stub = factorial_pb2.MathServiceStub(channel)
  response = stub.Factorial(factorial_pb2.FactorialRequest(n=requestedN))
  print("Factorial of {} is: {}".format(requestedN, response.result))

if __name__ == '__main__':
    while(True):
      run()
      time.sleep(5)
