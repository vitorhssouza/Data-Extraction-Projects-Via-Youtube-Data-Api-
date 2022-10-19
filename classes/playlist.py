from classes.conexao import Conexao
from chave_api import api_key

youtube = Conexao(api_key)


class Playlist:

    def __init__(self, url_playlist):
        self.__url_playlist = url_playlist
        self.__playlist = list()

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


