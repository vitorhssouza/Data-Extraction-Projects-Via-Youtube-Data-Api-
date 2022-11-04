import pandas as pd
from classes.estatistica import EstatisticaPlaylist

dados = EstatisticaPlaylist()


class EstruturaDataFrame:

    def __init__(self, titulo, id, descricao, data_publicacao, data_extracao, likes, visualizacao, comentario):
        self.__tituto = titulo
        self.__id = id
        self._descricao = descricao
        self.__data_publicacao = data_publicacao
        self._data_extracao = data_extracao
        self.__likes = likes
        self.__visualizacao = visualizacao
        self.__comentario = comentario




