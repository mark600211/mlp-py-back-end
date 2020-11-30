import os
from pathlib import Path

from synology_api import filestation, downloadstation
from ..grpc.client.module import Acts

url = os.getenv('SYN_URL')
port = os.getenv('SYN_PORT')
user = os.getenv('SYN_USER')
pasw = os.getenv('SYN_PASSWORD')

fl = filestation.FileStation(url, port, user, pasw)


class Synology():

    @staticmethod
    def uploadFile(file_path: Path, id: str):
        syn_path = Acts.getPath(id)

        syn_url = Path.joinpath('Portal', syn_path)

        up = fl.upload_file(syn_url, file_path)

        return { 'upload': up, 'synUrl': syn_url }
