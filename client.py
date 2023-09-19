import grpc

import multiply_pb2
import multiply_pb2_grpc

def run():
   with grpc.insecure_channel('localhost:50051') as channel:

      # creation of stub in client file to connect to server side stub
      stub = multiply_pb2_grpc.MultiplierStub(channel)

      # calling to remote procedure through the stub created and receiving a response
      response = stub.multiply(multiply_pb2.clientinput(num1=6, num2=8))
      
   print("Multiplier client received following from server:{}".format(response.product))
run()