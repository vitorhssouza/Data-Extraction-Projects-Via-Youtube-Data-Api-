from Classes.Playlist import Playlist
import matplotlib.pyplot as plt
import pandas as pd


class Graficos(Playlist):

    def __init__(self, url):
        super().__init__(url)

    def graph_visualizacoes(self):
        titulos = []

        for c in self.dataframe()['Titulo']:
            posicao = c.find('-')
            titulo = c[:posicao - 1]
            titulos.append(titulo)

        plt.figure(figsize=(15, 6))

        plt.bar(titulos, self.dataframe()['Visualizações'], color='#b5ffb0', edgecolor='white')

        plt.xticks(rotation=45, ha='right')

        return plt.show()

    def graph_likes(self):
        titulos = []

        for c in self.dataframe()['Titulo']:
            posicao = c.find('-')
            titulo = c[:posicao - 1]
            titulos.append(titulo)

        plt.figure(figsize=(10, 5))

        plt.bar(titulos, self.dataframe()['Like'], color='#b5ffb0', edgecolor='white')

        plt.xticks(rotation=45, ha='right')

        return plt.show()


    def graph_10(self):
        analise_playlist = self.dataframe().groupby(by=['Titulo']).sum().reset_index()[
            ['Titulo', 'Visualizações']].sort_values('Visualizações', ascending=False)

        # Top 10 videos com mais visualizações da playlist

        plt.figure(figsize=(20, 10))

        # titulo
        plt.title('Videos com maiores numeros de visualizações', loc='left', fontsize=18)

        # Gráficos
        plt.bar(analise_playlist['Titulo'][:10].values, analise_playlist['Visualizações'][:10].values, color='#f44e3f')

        # labels
        plt.ylabel('Quantidade de Visualização', fontsize=14)
        plt.xticks(rotation=90)

        return plt.show()

    def graph_relacao(self):

        titulos = []

        for c in self.dataframe()['Titulo']:
            posicao = c.find('-')
            titulo = c[:posicao - 1]
            titulos.append(titulo)

        plt.figure(figsize=(20, 10))
        plt.bar(titulos, self.dataframe()['Visualizações'], color='#b5ffb0', edgecolor='white')
        plt.bar(titulos, self.dataframe()['Like'])

        plt.xticks(rotation=45, ha='right')

        return plt.show()

