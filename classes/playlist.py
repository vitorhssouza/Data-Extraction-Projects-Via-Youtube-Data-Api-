from classes.conexao import Conexao
from chave_api import api_key

youtube = Conexao(api_key)
nextPage_token = None


class Playlist:

    def __init__(self, url_playlist):
        self.__url_playlist = url_playlist
        self.__playlist = list()

    @property
    def playlist(self):
        while True:
            filtro = youtube.conexao.playlistItems().list(part='snippet', playlistId=api_key, maxResults=50,
                                                          pageToken=nextPage_token).execute()
            self.__playlist += filtro['items']
            nextPage_token = filtro.get('nestPageToken')

            if nextPage_token is None:
                break
        return self.__playlist


