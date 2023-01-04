import pandas as pd

from Classes.Conexao import Conexao

youtube = Conexao.conexao()


class Playlist:

    def __init__(self, url):
        self.__url = url


    def playlist_video(self):
        self.__playlist = list()
        nextPage_token = None
        while True:
            resultado = youtube.playlistItems().list(part='snippet', playlistId=self.__url, maxResults=50,
                                                     pageToken=nextPage_token).execute()
            self.__playlist += resultado['items']

            nextPage_token = resultado.get('nestPageToken')

            if nextPage_token is None:
                break

        return self.__playlist


    def id_videos(self):
        self.__id_videos = list(map(lambda video: video['snippet']['resourceId']['videoId'], self.playlist_video()))
        return self.__id_videos


    def estatistica(self):
        self.__estatistica = list()

        for video_id in self.id_videos():
            result = youtube.videos().list(part='statistics', id=video_id).execute()
            self.__estatistica += result['items']

        return self.__estatistica

    def link(self):
        self.__link = list()
        for c in self.id_videos():
            self.__link.append(f'https://www.youtube.com/watch?v={c}&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=2&t=1511s')
        return self.__link

    def titulo_video(self):
        self.__titulo_video = list(map(lambda x: x['snippet']['title'], self.playlist_video()))
        return self.__titulo_video

    def data_publicacao(self):
        self.__data_publicacao = list(map(lambda x: str(x['snippet']['publishedAt'])[:10], self.playlist_video()))
        return self.__data_publicacao

    def descricao_video(self):
        self.__descricao = list(map(lambda x: x['snippet']['description'], self.playlist_video()))
        return self.__descricao

    def video_id(self):
        self.__video_id = list(map(lambda x: x['snippet']['resourceId']['videoId'], self.playlist_video()))
        return self.__video_id

    def like(self):
        self.__like = list(map(lambda x: int(x['statistics']['likeCount']), self.estatistica()))
        return self.__like

    def visualizacoes(self):
        self.__visualizacoes = list(map(lambda x: int(x['statistics']['viewCount']), self.estatistica()))
        return self.__visualizacoes

    def comentarios(self):
        self.__comentarios = list(map(lambda x: int(x['statistics']['commentCount']), self.estatistica()))
        return self.__comentarios

    def dataframe(self):
        self.__dataframe = pd.DataFrame({
            'Titulo': self.titulo_video(),
            'Id Video': self.id_videos(),
            'Descrição Video': self.descricao_video(),
            'Data Publicação': self.data_publicacao(),
            'Like': self.like(),
            'Visualizações': self.visualizacoes(),
            'Comentarios': self.comentarios(),
            'URL dos videos': self.link()
        })

        return self.__dataframe
