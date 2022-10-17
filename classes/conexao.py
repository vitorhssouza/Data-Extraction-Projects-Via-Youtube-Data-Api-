from googleapiclient.discovery import build
from chave_api import api_key


class Conexao:
    def __init__(self, chave):
        self.__chave = chave
        self.__youtube = ''

    @property
    def conexao(self):
        self.__youtube = (build('youtube', 'v3', developerKey=self.__chave))
        return self.__youtube


youtube = Conexao(api_key)

