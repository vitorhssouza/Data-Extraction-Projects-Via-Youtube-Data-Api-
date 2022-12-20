# Classe onde contém todos os map para colocar os dados da estatistica em um dataframe
from classes.playlist import Playlist
from datetime import datetime
import pandas as pd


class EstatisticaPlaylist(Playlist):
    def __init__(self, url_playlist):
        super().__init__(url_playlist)
        self.__titulos_videos = list(map(lambda x: x['snippet']['title'], self.playlist))

        self.__data_publicacoes = list(map(lambda x: str(x['snippet']['publishedAt'])[:10], self.playlist))

        self.__data_extracao = [str(datetime.now().strftime('%d/%m/%Y'))] * len(self.id_videos)

        self.__descricao_videos = list(map(lambda x: x['snippet']['description'], self.playlist))

        self.__id_videos = list()

        self.__likes = list(map(lambda x: int(x['statistics']['likeCount']), self.estatisticas_videos))

        self.__visualizacoes = list(map(lambda x: int(x['statistics']['viewCount']), self.estatisticas_videos))

        self.__comentarios = list(map(lambda x: int(x['statistics']['commentCount']), self.estatisticas_videos))

        self.__df = pd.DataFrame({
            'Título': self.__titulos_videos,
            'Id Video': self.id_videos,
            'Descricao do Video': self.__descricao_videos,
            'Data de Publicacao': self.__data_publicacoes,
            'Data de Extração': self.__data_extracao,
            'Likes': self.__likes,
            'Visualizações': self.__visualizacoes,
            'Comentarios': self.__comentarios,
            'Url dos Videos': self.url_videos

        })

    """@property
    def titulos_videos(self):
        #self.__titulos_videos = list(map(lambda x: x['snippet']['title'], self.playlist))
        return self.__titulos_videos

    @property
    def data_publicacao(self):
        #self.__data_publicacoes = list(map(lambda x: str(x['snippet']['publishedAt'])[:10],
                                       #self.playlist))
        return self.__data_publicacoes

    @property
    def descricao_videos(self):
        #self.__descricao_videos = list(map(lambda x: x['snippet']['description'], self.playlist))
        return self.__descricao_videos

    @property
    def likes(self):
        #self.__likes = list(map(lambda x: int(x['statistics']['likeCount']), self.estatisticas_videos))
        return self.__likes

    @property
    def visualizacao(self):
        #self.__visualizacoes = list(map(lambda x: int(x['statistics']['viewCount']), self.estatisticas_videos))
        return self.__visualizacoes

    @property
    def comentarios(self):
        #self.__comentarios = list(map(lambda x: int(x['statistics']['commentCount']), self.estatisticas_videos))
        return self.__comentarios

    @property
    def dataframe(self):
        self.__df = pd.DataFrame({
            'Título': self.titulos_videos,
            'Id Video': self.id_videos,
            'Descricao do Video': self.descricao_videos,
            'Data de Publicacao': self.data_publicacao,
            'Data de Extração': self.data_publicacao,
            'Likes': self.likes,
            'Visualizações': self.visualizacao,
            'Comentarios': self.comentarios,
            'Url dos Videos': self.url_videos
        })

        return self.__df
"""

"""d = EstatisticaPlaylist('PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6')
print(d.dataframe)"""
