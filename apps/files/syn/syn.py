import os
from pathlib import Path

from synology_api import filestation, downloadstation

url = os.getenv('SYN_URL')
port = os.getenv('SYN_PORT')
user = os.getenv('SYN_USER')
pasw = os.getenv('SYN_PASSWORD')

fl = filestation.FileStation(url, port, user, pasw)


class Synology():

    @staticmethod
    def uploadFile(path: Path, filename: str):
        up = fl.upload_file(f'Portal/{filename}', path)

        return up
