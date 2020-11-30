from os import error
import grpc
from ..generated import acts_pb2_grpc, acts_pb2

def getStub():
    try:
        channel = grpc.insecure_channel('localhost:50052')
        stub = acts_pb2_grpc.ActsServiceStub(channel)
        
    except(error):
        print(error.strerror)
    
    return stub

def getPath(id: str):
    try:
        stub = getStub()
        path = stub.GetFilePath({ 'id': id })

    except(error):
        print(error.strerror)

    return path

def getAct(id: str):
    try:
        stub = getStub()
        act = stub.getActForTemplater({ 'id': id })
    except(error):
        print(error.strerror)

    return act