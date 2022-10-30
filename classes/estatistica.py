# Classe onde contém todos os map para colocar os dados da estatistica em um dataframe
from classes.playlist import Playlist
from classes.videos import Videos


class EstatisticaPlaylist(Playlist):
    def __init__(self, url_playlist):
        super().__init__(url_playlist)
        self.__titulos_videos = list()
        self.__data_publicacoes = list()
        self.__descricao_videos = list()
        self.__id_videos = list()
        self.__likes = list()
        self.__visualizacoes = list()
        self.__comentarios = list()

    @property
    def titulos_videos(self):
        self.__titulos_videos = list(map(lambda x: x['snippet']['title'], self.playlist))
        return self.__titulos_videos

    @property
    def data_publicacao(self):
        self.__data_publicacoes = list(map(lambda x: str(x['snippet']['publishedAt'])[:10],
                                       self.playlist))
        return self.__data_publicacoes

    @property
    def descricao_videos(self):
        self.__descricao_videos = list(map(lambda x: x['snippet']['description'], self.playlist))
        return self.__descricao_videos

    @property
    def id_videos(self):
        self.__id_videos = list(map(lambda x: x['snippet']['resourceId']['videoId'], self.playlist))
        return self.__id_videos

    @property
    def likes(self):
        self.__likes = list(map(lambda x: int(x['statistics']['likeCount']), self.estatisticas_videos))
        return self.__likes

    @property
    def visualizao(self):
        self.__visualizacoes = list(map(lambda x: int(x['statistics']['viewCount']), self.estatisticas_videos))
        return self.__visualizacoes

    @property
    def comentarios(self):
        self.__comentarios = list(map(lambda x: int(x['statistics']['commentCount']), self.estatisticas_videos))
        return self.__comentarios
