from concurrent import futures

import grpc
import multiply_pb2
import multiply_pb2_grpc

# creating a service at server side and defining the body of remote procedure
class Multiplier(multiply_pb2_grpc.MultiplierServicer):
   def multiply(self, request, context):
      print("Got request to multiply {} and {}".format(request.num1,request.num2))
      return multiply_pb2.multipliedoutput(product=request.num1*request.num2)


# defining a server
def server():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

   # linking the service to server
   multiply_pb2_grpc.add_MultiplierServicer_to_server(Multiplier(), server)
   server.add_insecure_port('[::]:50051')
   print("gRPC starting")
   server.start()
   server.wait_for_termination()
server()