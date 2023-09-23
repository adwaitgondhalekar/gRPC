from concurrent import futures
import signal
import threading

import grpc
import multiply_pb2
import multiply_pb2_grpc

flag = False

# creating a service at server side and defining the body of remote procedure
class Multiplier(multiply_pb2_grpc.MultiplierServicer):
   def multiply(self, request, context):
      print("Got request to multiply {} and {}".format(request.num1,request.num2))
      return multiply_pb2.multipliedoutput(product=request.num1*request.num2,message="Hello this is server !")


# defining a server
def server():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

   # linking the service to server
   multiply_pb2_grpc.add_MultiplierServicer_to_server(Multiplier(), server)
   server.add_insecure_port('[::]:50051')
   print("gRPC starting")
   server.start()
   #

   done = threading.Event()

   def on_done(signum, frame):
      #logger.info('Got signal {}, {}'.format(signum, frame))
      done.set()
   
   # signal.signal(signal.SIGTERM, on_done)
   # done.wait()
   
   server.wait_for_termination()

server()
print("reached here")
while True:
   pass