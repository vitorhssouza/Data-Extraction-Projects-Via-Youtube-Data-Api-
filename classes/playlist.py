from classes.conexao import Conexao
from chave_api import api_key
import pandas as pd

youtube = Conexao(api_key)


class Playlist:

    def __init__(self, url_playlist):
        self.__url_playlist = url_playlist
        self.__playlist = list()
        self.__id_videos = list(map(lambda video: video['snippet']['resourceId']['videoId'], self.playlist))
        self.__estatisticas_playlist = list()
        self.__url_videos = list()

        self.__titulos_videos = list(map(lambda x: x['snippet']['title'], self.playlist))
        self.__likes = list(map(lambda x: int(x['statistics']['likeCount']), self.estatisticas_videos))


    @property
    def playlist(self):
        next_page_token = None
        while True:
            filtro = youtube.conexao.playlistItems().list(part='snippet', playlistId=self.__url_playlist, maxResults=50,
                                                          pageToken=next_page_token).execute()
            self.__playlist += filtro['items']
            next_page_token = filtro.get('nestPageToken')

            if next_page_token is None:
                break
        return self.__playlist

    @property
    def id_videos(self):
        self.__id_videos = list(map(lambda video: video['snippet']['resourceId']['videoId'], self.playlist))
        return self.__id_videos

    @property
    def estatisticas_videos(self):
        for id_video in self.id_videos:
            filtro = youtube.conexao.videos().list(part='statistics', id=id_video).execute()
            self.__estatisticas_playlist += filtro['items']
        return self.__estatisticas_playlist

    @property
    def url_videos(self):
        for url in self.id_videos:
            self.__url_videos.append(f'https://www.youtube.com/watch?v={url}&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=2&t=1511s')
        return self.__url_videos

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
    def likes(self):
        self.__likes = list(map(lambda x: int(x['statistics']['likeCount']), self.estatisticas_videos))
        return self.__likes

    @property
    def visualizacao(self):
        self.__visualizacoes = list(map(lambda x: int(x['statistics']['viewCount']), self.estatisticas_videos))
        return self.__visualizacoes

    @property
    def comentarios(self):
        self.__comentarios = list(map(lambda x: int(x['statistics']['commentCount']), self.estatisticas_videos))
        return self.__comentarios

    @property
    def dataframe(self):
        self.__df = pd.DataFrame({
            'Título': self.__titulos_videos,
            'Id Video': self.__id_videos,
            'Likes': self.__likes

        })

        return self.__df

