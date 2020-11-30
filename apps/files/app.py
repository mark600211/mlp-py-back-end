from concurrent import futures
import logging
import grpc
import logging
from .settings import Settings

from .grpc.generated import python_files_pb2_grpc
from .grpc.service import Files


class Server:

    @staticmethod
    def run():
        logging.basicConfig()

        Settings()

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=500))

        python_files_pb2_grpc.add_PythonFilesServiceServicer_to_server(
            Files(), server)

        server.add_insecure_port('[::]:50150')

        server.start()

        print('server start and running')

        server.wait_for_termination()
