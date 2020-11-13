import os
from os import error
from pathlib import Path
import uuid

from ..generated import python_files_pb2, python_files_pb2_grpc

from ...syn.syn import Synology


class Files(python_files_pb2_grpc.PythonFilesServiceServicer):

    def UploadFile(self, request_iterator, context):
        docId = None
        filename = None
        path = None
        f = None
        err = None
        resData = None

        try:
            tmp = str(uuid.uuid4())

            tmp_path = Path.cwd() / 'files' / 'tmp' / tmp

            f = open(tmp_path, 'wb')

            for req in request_iterator:
                if (req.metadata.id):
                    data = req.metadata
                    meta = data.upload_metadata

                    docId = data.id
                    filename = meta.filename

                    path = Path.cwd() / 'files' / 'tmp' / filename
                else:
                    chunk = req.chunk
                    f.write(chunk)

            f.close()

            os.rename(tmp_path, path)

            uploaded = Synology.uploadFile(path, filename)

            if uploaded[1]['success'] == False:
                code = str(uploaded[1]['error']['code'])
                err = f'Synology return an error with code: {code}'

                err_path = Path.cwd() / 'files' / 'tmp' / docId

                os.rename(path, err_path)
            else:
                resData = {'docId': docId, "synUrl": 't'}

                os.remove(path)
        except(error):
            err(error.strerror)

        return python_files_pb2.Response(resData=resData, error=err)
