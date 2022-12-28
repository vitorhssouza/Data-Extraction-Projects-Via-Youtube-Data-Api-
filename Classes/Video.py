from Classes.Conexao import Conexao
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt


class Video:

    def __init__(self, url):
        self.__url = url

    def comentario(self):
        self.__requests = Conexao.conexao().commentThreads().list(
            part="snippet",
            videoId=self.__url,
            maxResults=100
        )

        self.__response = self.__requests.execute()

        return self.__response

    def dataframe(self):
        self.__df = pd.json_normalize(self.comentario()['items'])

        self.__df = self.__df[['snippet.topLevelComment.snippet.textDisplay', 'snippet.topLevelComment.snippet.publishedAt']]

        self.__df.rename(columns={'snippet.topLevelComment.snippet.textDisplay':'Comentários', 'snippet.topLevelComment.snippet.publishedAt': 'Data de Publicação'},inplace=True)

        self.__df['Comentários'] = self.__df['Comentários'].str.lower()

        self.__df['Quant_palavras'] = self.__df['Comentários'].str.split().str.len()

        self.__df = self.__df[self.__df['Quant_palavras'] > 5]

        return self.__df

    def graph_nuvem(self):

        self.__lista = list()

        for c in self.dataframe()['Comentários']:
            self.__lista.append(c)

        lista = [' ','', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para',
               'é', 'com', 'não', 'uma', 'os', 'no', 'se','na', 'por', 'mais',
               'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem',
               'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos',
               'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso',
               'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus',  'quem']

        lista_stop = 'de a o que e do da em um para é com não uma os no se na por mais as dos como mas foi ao ele das tem à seu sua ou ser quando muito há nos já está eu também só pelo pela até isso ela entre depois sem mesmo aos ter seus quem'

        lista2_stopwords = 'nas me esse eles estão você tinha foram essa num nem suas meu às minha têm numa pelos ' \
                           'elas havia seja qual será nós tenho lhe deles essas esses pelas este fosse dele tu te ' \
                           'vocês vos lhes meus minhas teu tua teus tuas nosso nossa nossos nossas dela delas esta ' \
                           'estes estas aquele aquela aqueles aquelas isto aquilo estou está estamos estão estive ' \
                           'esteve estivemos estiveram estava estávamos estavam estivera estivéramos esteja estejamos ' \
                           'estejam estivesse estivéssemos estivessem estiver estivermos estiverem hei há havemos ' \
                           'hão houve houvemos houveram houvera houvéramos haja hajamos hajam houvesse houvéssemos ' \
                           'houvessem houver houvermos houverem houverei houverá houveremos houverão houveria ' \
                           'houveríamos houveriam sou somos são era éramos eram fui foi fomos foram fora fôramos ' \
                           'seja sejamos sejam fosse fôssemos fossem for formos forem serei será seremos serão seria ' \
                           'seríamos seriam tenho tem temos tém tinha tínhamos tinham tive teve tivemos tiveram tivera ' \
                           'tivéramos tenha tenhamos tenham tivesse tivéssemos tivessem tiver tivermos tiverem terei ' \
                           'terá teremos terão teria teríamos teriam '

        self.__stopwords = set(STOPWORDS)

        self.__l = lista_stop + lista2_stopwords

        self.__l = self.__l.split(' ')

        self.__l = self.__l + lista

        self.__stopwords.update(self.__l)

        self.__nuvens = WordCloud(width=500, height=200, stopwords=self.__stopwords, scale=3, repeat=True,
                           background_color='white').generate(str(self.__lista))

        plt.figure(figsize=(40, 10),
                   facecolor='k',
                   edgecolor='k')

        plt.imshow(self.__nuvens, interpolation='bilinear')
        plt.axis('off')

        return plt.show()

