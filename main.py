"""
🎬 Sistema de Recomendação de Filmes - Machine Learning

Este é meu projeto de aprendizado sobre sistemas de recomendação.
Implementei um Content-Based Filtering usando TF-IDF e Cosine Similarity.

Autor: Pedro Vergueiro
Objetivo: Entender como funcionam os algoritmos de recomendação
Técnica: Content-Based Filtering (filtragem baseada em conteúdo)
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class RecomendadorFilmes:
    """
    Sistema de Recomendação de Filmes usando Machine Learning
    
    Esta classe implementa um sistema de recomendação baseado em conteúdo.
    O que aprendi implementando isso:
    - Como transformar dados categóricos em vetores numéricos
    - Como calcular similaridade entre itens
    - Como construir um pipeline completo de ML
    """
    
    def __init__(self):
        """
        Inicializa o sistema de recomendação.
        
        Atributos que aprendi a usar:
        - dados: DataFrame com informações dos filmes
        - matriz_similaridade: Matriz com similaridades entre todos os filmes
        - indices: Mapeamento de título para índice (para busca rápida)
        """
        self.dados = None
        self.matriz_similaridade = None
        self.indices = None
        self.vectorizer = None  # Guarda o vectorizer treinado
        
    def carregar_dados(self):
        """
        📊 Carrega e prepara os dados dos filmes
        
        O que aprendi sobre preparação de dados:
        - Importância de ter dados estruturados
        - Como combinar diferentes features (gênero + diretor)
        - Feature engineering: criar novas características úteis
        """
        print("📊 Carregando dados dos filmes...")
        
        # Dataset criado por mim para aprendizado
        # Em um projeto real, isso viria de uma API ou banco de dados
        filmes = {
            'titulo': [
                'O Poderoso Chefão', 'Pulp Fiction', 'O Senhor dos Anéis', 
                'Matrix', 'Clube da Luta', 'Forrest Gump', 'Interestelar',
                'Os Suspeitos', 'Cidade de Deus', 'Gladiador',
                'Toy Story', 'Procurando Nemo', 'Shrek', 'Os Incríveis',
                'Avatar', 'Star Wars', 'Harry Potter', 'Vingadores',
                'Blade Runner', 'Alien', 'Terminator', 'De Volta para o Futuro'
            ],
            'genero': [
                'Crime,Drama', 'Crime,Drama', 'Aventura,Fantasia',
                'Ação,Ficção', 'Drama', 'Drama,Romance', 'Ficção,Aventura',
                'Crime,Suspense', 'Crime,Drama', 'Ação,Drama',
                'Animação,Comédia', 'Animação,Aventura', 'Animação,Comédia',
                'Animação,Ação', 'Ficção,Aventura', 'Ficção,Aventura',
                'Fantasia,Aventura', 'Ação,Ficção', 'Ficção,Drama',
                'Ficção,Terror', 'Ação,Ficção', 'Ficção,Comédia'
            ],
            'diretor': [
                'Francis Ford Coppola', 'Quentin Tarantino', 'Peter Jackson',
                'Wachowski', 'David Fincher', 'Robert Zemeckis', 'Christopher Nolan',
                'Bryan Singer', 'Fernando Meirelles', 'Ridley Scott',
                'John Lasseter', 'Andrew Stanton', 'Andrew Adamson', 'Brad Bird',
                'James Cameron', 'George Lucas', 'Chris Columbus', 'Joss Whedon',
                'Ridley Scott', 'Ridley Scott', 'James Cameron', 'Robert Zemeckis'
            ],
            'ano': [
                1972, 1994, 2001, 1999, 1999, 1994, 2014,
                1995, 2002, 2000, 1995, 2003, 2001, 2004,
                2009, 1977, 2001, 2012, 1982, 1979, 1984, 1985
            ]
        }
        
        # Criando DataFrame - estrutura fundamental para ML
        self.dados = pd.DataFrame(filmes)
        
        # FEATURE ENGINEERING: Combinando características
        # Esta é uma técnica fundamental em ML!
        self.dados['caracteristicas'] = (
            self.dados['genero'] + ',' + 
            self.dados['diretor']
        )
        
        print(f"✅ {len(self.dados)} filmes carregados com sucesso!")
        
    def treinar_modelo(self):
        """
        🤖 Treina o modelo de recomendação
        
        O que aprendi sobre treinamento de modelos:
        - TF-IDF: Como transformar texto em vetores numéricos
        - Cosine Similarity: Como medir similaridade entre vetores
        - Pipeline de ML: Preparação → Treinamento → Predição
        """
        print("🤖 Treinando modelo de recomendação...")
        
        # PASSO 1: VETORIZAÇÃO COM TF-IDF
        # TF-IDF = Term Frequency - Inverse Document Frequency
        # Transforma texto em números de forma inteligente
        self.vectorizer = TfidfVectorizer(
            stop_words='english',  # Remove palavras comuns
            lowercase=True,        # Padroniza para minúsculas
            token_pattern=r'\b\w+\b'  # Define como separar palavras
        )
        
        # Transforma as características em uma matriz numérica
        # Cada filme vira um vetor de números
        matriz_tfidf = self.vectorizer.fit_transform(self.dados['caracteristicas'])
        
        print(f"📐 Matriz TF-IDF criada: {matriz_tfidf.shape}")
        print(f"   - {matriz_tfidf.shape[0]} filmes")
        print(f"   - {matriz_tfidf.shape[1]} características únicas")
        
        # PASSO 2: CÁLCULO DE SIMILARIDADE
        # Cosine Similarity mede o ângulo entre vetores
        # Valores de 0 (nada similar) a 1 (idêntico)
        self.matriz_similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)
        
        # PASSO 3: CRIAÇÃO DO ÍNDICE
        # Mapeia título do filme para posição na matriz (busca rápida)
        self.indices = pd.Series(
            self.dados.index, 
            index=self.dados['titulo']
        ).drop_duplicates()
        
        print("✅ Modelo treinado com sucesso!")
        print(f"📊 Matriz de similaridade: {self.matriz_similaridade.shape}")
    
    def recomendar(self, titulo_filme, num_recomendacoes=5):
        """
        🎯 Gera recomendações para um filme
        
        O que aprendi sobre geração de recomendações:
        - Como usar a matriz de similaridade
        - Importância de ordenar por relevância
        - Tratamento de erros (filme não encontrado)
        
        Args:
            titulo_filme (str): Nome do filme para recomendar similares
            num_recomendacoes (int): Quantas recomendações retornar
            
        Returns:
            pd.Series ou str: Lista de filmes recomendados ou mensagem de erro
        """
        try:
            # PASSO 1: Encontrar o índice do filme
            idx = self.indices[titulo_filme]
            
            # PASSO 2: Pegar similaridades deste filme com todos os outros
            similaridades = list(enumerate(self.matriz_similaridade[idx]))
            
            # PASSO 3: Ordenar por similaridade (maior primeiro)
            # [1:] remove o próprio filme da lista
            similaridades = sorted(similaridades, key=lambda x: x[1], reverse=True)
            
            # PASSO 4: Pegar os índices dos filmes mais similares
            indices_filmes = [i[0] for i in similaridades[1:num_recomendacoes+1]]
            
            # PASSO 5: Retornar os títulos dos filmes recomendados
            recomendacoes = self.dados['titulo'].iloc[indices_filmes]
            
            # Adicionar scores de similaridade para análise
            scores = [round(similaridades[i+1][1], 3) for i in range(num_recomendacoes)]
            
            return recomendacoes, scores
            
        except KeyError:
            return f"❌ Filme '{titulo_filme}' não está na base de dados.", None
    
    def explorar_dados(self):
        """
        🔍 Explora e analisa os dados carregados
        
        O que aprendi sobre análise exploratória:
        - Importância de entender os dados antes do ML
        - Como identificar padrões e distribuições
        - Visualização básica de informações
        """
        print("\n" + "="*60)
        print("🔍 ANÁLISE EXPLORATÓRIA DOS DADOS")
        print("="*60)
        
        print(f"📊 Total de filmes: {len(self.dados)}")
        print(f"📅 Período: {self.dados['ano'].min()} - {self.dados['ano'].max()}")
        
        print("\n📋 Primeiros 5 filmes:")
        print(self.dados[['titulo', 'genero', 'diretor', 'ano']].head())
        
        print(f"\n🎭 Gêneros únicos encontrados:")
        generos_unicos = set()
        for generos in self.dados['genero']:
            generos_unicos.update(generos.split(','))
        print(f"   Total: {len(generos_unicos)} gêneros")
        for genero in sorted(generos_unicos):
            print(f"   - {genero}")
        
        print(f"\n🎬 Diretores únicos: {self.dados['diretor'].nunique()}")
        diretores_freq = self.dados['diretor'].value_counts()
        print("   Top 3 diretores com mais filmes:")
        for diretor, count in diretores_freq.head(3).items():
            print(f"   - {diretor}: {count} filme(s)")
    
    def analisar_similaridade(self, filme1, filme2):
        """
        🔬 Analisa a similaridade entre dois filmes específicos
        
        Útil para entender como o algoritmo funciona.
        """
        try:
            idx1 = self.indices[filme1]
            idx2 = self.indices[filme2]
            
            similaridade = self.matriz_similaridade[idx1][idx2]
            
            print(f"\n🔬 ANÁLISE DE SIMILARIDADE")
            print(f"🎬 Filme 1: {filme1}")
            print(f"   Gênero: {self.dados.iloc[idx1]['genero']}")
            print(f"   Diretor: {self.dados.iloc[idx1]['diretor']}")
            
            print(f"🎬 Filme 2: {filme2}")
            print(f"   Gênero: {self.dados.iloc[idx2]['genero']}")
            print(f"   Diretor: {self.dados.iloc[idx2]['diretor']}")
            
            print(f"📊 Similaridade: {similaridade:.3f}")
            
            if similaridade > 0.7:
                print("✅ Filmes muito similares!")
            elif similaridade > 0.4:
                print("🔶 Filmes moderadamente similares")
            else:
                print("❌ Filmes pouco similares")
                
        except KeyError as e:
            print(f"❌ Filme não encontrado: {e}")

def main():
    """
    🚀 Função principal - demonstra o sistema funcionando
    
    Aqui mostro como usar o sistema completo de recomendação.
    """
    print("🎬" + "="*59)
    print("🎬 SISTEMA DE RECOMENDAÇÃO DE FILMES - PEDRO VERGUEIRO")
    print("🎬" + "="*59)
    print("🤖 Usando Machine Learning para recomendar filmes!")
    print("📚 Técnicas: TF-IDF + Cosine Similarity")
    
    # Inicializar o sistema
    recomendador = RecomendadorFilmes()
    
    # Pipeline completo de ML
    recomendador.carregar_dados()
    recomendador.treinar_modelo()
    recomendador.explorar_dados()
    
    # Demonstração com filmes de diferentes gêneros
    filmes_teste = [
        'Matrix',           # Ficção científica
        'Toy Story',        # Animação
        'Cidade de Deus',   # Drama nacional
        'O Poderoso Chefão' # Crime clássico
    ]
    
    print("\n" + "="*60)
    print("🎯 DEMONSTRAÇÃO DE RECOMENDAÇÕES")
    print("="*60)
    
    for filme in filmes_teste:
        print(f"\n🎬 Se você gostou de '{filme}', recomendo:")
        
        resultado = recomendador.recomendar(filme, num_recomendacoes=3)
        
        if isinstance(resultado[0], pd.Series):
            recomendacoes, scores = resultado
            for i, (titulo, score) in enumerate(zip(recomendacoes, scores), 1):
                print(f"   {i}. {titulo} (similaridade: {score})")
        else:
            print(f"   {resultado[0]}")
    
    # Análise de similaridade entre filmes específicos
    print("\n" + "="*60)
    print("🔬 ANÁLISE DETALHADA DE SIMILARIDADE")
    print("="*60)
    
    # Comparar filmes similares
    recomendador.analisar_similaridade("Matrix", "Interestelar")
    recomendador.analisar_similaridade("Toy Story", "Procurando Nemo")
    
    # Comparar filmes diferentes
    recomendador.analisar_similaridade("Matrix", "Toy Story")
    
    print("\n🎉 Demonstração concluída!")
    print("💡 Experimente modificar o código para adicionar mais filmes!")

if __name__ == "__main__":
    main()
