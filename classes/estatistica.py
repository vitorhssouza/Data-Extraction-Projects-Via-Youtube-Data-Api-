# Classe onde contém todos os map para colocar os dados da estatistica em um dataframe
from classes.playlist import Playlist
from classes.videos import Videos


class Estatistica(Playlist, Videos):
    def __init__(self, url_playlist, url_videos):
        super().__init__(url_playlist)
        super().__init__(url_videos)

        self.__titulos_videos = list()
        self.__data_publicacoes = list()
        self.__descricao_videos = list()
        self.__id_videos = list()
        self.__likes = list()
        self.__visualizacoes = list()
        self.__comentarios = list()

    @property
    def titulos_videos(self):
        self.__titulos_videos = map(lambda x: x['snippet']['title'], self.playlist)
        return self.__titulos_videos
