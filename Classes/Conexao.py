from chave_api import api_key
from googleapiclient.discovery import build


class Conexao:

    @staticmethod
    def conexao():
        youtube = (build('youtube', 'v3', developerKey=api_key))
        return youtube


