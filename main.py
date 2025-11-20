import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class RecomendadorFilmes:
    def __init__(self):
        self.dados = None
        self.matriz_similaridade = None
        self.indices = None
        
    def carregar_dados(self):
        filmes = {
            'titulo': [
                'O Poderoso Chefão', 'Pulp Fiction', 'O Senhor dos Anéis', 
                'Matrix', 'Clube da Luta', 'Forrest Gump', 'Interestelar',
                'Os Suspeitos', 'Cidade de Deus', 'Gladiador',
                'Toy Story', 'Procurando Nemo', 'Shrek', 'Os Incríveis',
                'Avatar', 'Star Wars', 'Harry Potter', 'Vingadores'
            ],
            'genero': [
                'Crime,Drama', 'Crime,Drama', 'Aventura,Fantasia',
                'Ação,Ficção', 'Drama', 'Drama,Romance', 'Ficção,Aventura',
                'Crime,Suspense', 'Crime,Drama', 'Ação,Drama',
                'Animaçao,Comédia', 'Animaçao,Aventura', 'Animaçao,Comédia',
                'Animaçao,Ação', 'Ficção,Aventura', 'Ficção,Aventura',
                'Fantasia,Aventura', 'Ação,Ficção'
            ],
            'diretor': [
                'Francis Ford Coppola', 'Quentin Tarantino', 'Peter Jackson',
                'Wachowski', 'David Fincher', 'Robert Zemeckis', 'Christopher Nolan',
                'Bryan Singer', 'Fernando Meirelles', 'Ridley Scott',
                'John Lasseter', 'Andrew Stanton', 'Andrew Adamson', 'Brad Bird',
                'James Cameron', 'George Lucas', 'Chris Columbus', 'Joss Whedon'
            ]
        }
        
        self.dados = pd.DataFrame(filmes)
        self.dados['caracteristicas'] = self.dados['genero'] + ',' + self.dados['diretor']
        
    def treinar_modelo(self):
        vectorizer = TfidfVectorizer(stop_words='english')
        matriz = vectorizer.fit_transform(self.dados['caracteristicas'])
        self.matriz_similaridade = cosine_similarity(matriz, matriz)
        self.indices = pd.Series(self.dados.index, index=self.dados['titulo']).drop_duplicates()
    
    def recomendar(self, titulo_filme, num_recomendacoes=5):
        try:
            idx = self.indices[titulo_filme]
            similaridades = list(enumerate(self.matriz_similaridade[idx]))
            similaridades = sorted(similaridades, key=lambda x: x[1], reverse=True)
            indices_filmes = [i[0] for i in similaridades[1:num_recomendacoes+1]]
            return self.dados['titulo'].iloc[indices_filmes]
            
        except KeyError:
            return f"Filme '{titulo_filme}' não está na base."
    
    def explorar_dados(self):
        print("=== EXPLORAÇÃO DOS DADOS ===")
        print(f"Total de filmes: {len(self.dados)}")
        print("\nPrimeiros 5 filmes:")
        print(self.dados[['titulo', 'genero']].head())
        print("\nGêneros únicos:", self.dados['genero'].unique())

def main():
    recomendador = RecomendadorFilmes()
    recomendador.carregar_dados()
    recomendador.treinar_modelo()
    recomendador.explorar_dados()
    
    print("\n" + "="*50)
    print("🎬 SISTEMA DE RECOMENDAÇÃO DE FILMES")
    print("="*50)

    filmes_teste = ['Matrix', 'Toy Story', 'Cidade de Deus']
    
    for filme in filmes_teste:
        print(f"\nSe você gostou de '{filme}', você provavelmente gosta de:")
        recomendacoes = recomendador.recomendar(filme)
        
        if isinstance(recomendacoes, pd.Series):
            for i, titulo in enumerate(recomendacoes, 1):
                print(f"   {i}. {titulo}")
        else:
            print(f"   {recomendacoes}")

if __name__ == "__main__":
    main()
