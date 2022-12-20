from classes.estatistica import EstatisticaPlaylist
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


class Graficos(EstatisticaPlaylist):

    def __init__(self, url):
        super().__init__(url)
        self.__grafico_linha = plt.bar(self.titulos_videos, self.__df)
