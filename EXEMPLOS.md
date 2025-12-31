# 📚 Exemplos de Uso do Sistema de Recomendação

Este arquivo contém exemplos práticos de como usar meu sistema de recomendação de filmes com Machine Learning.

## 🚀 Executando o Sistema

### Método Básico
```bash
# Executar o sistema completo
python main.py
```

### Método Interativo (Python)
```python
from main import RecomendadorFilmes

# Criar e treinar o sistema
recomendador = RecomendadorFilmes()
recomendador.carregar_dados()
recomendador.treinar_modelo()

# Fazer recomendações
recomendacoes, scores = recomendador.recomendar("Matrix", 5)
print(recomendacoes)
```

## 🎬 Exemplos de Recomendações

### 1. Filmes de Ficção Científica
```python
# Se você gostou de Matrix
recomendacoes, scores = recomendador.recomendar("Matrix")

# Resultado esperado:
# 1. Interestelar (0.856)
# 2. Avatar (0.743) 
# 3. Star Wars (0.721)
# 4. Blade Runner (0.698)
# 5. Alien (0.654)
```

### 2. Filmes de Animação
```python
# Se você gostou de Toy Story
recomendacoes, scores = recomendador.recomendar("Toy Story")

# Resultado esperado:
# 1. Os Incríveis (0.892)
# 2. Procurando Nemo (0.834)
# 3. Shrek (0.798)
```

### 3. Filmes de Crime/Drama
```python
# Se você gostou de Cidade de Deus
recomendacoes, scores = recomendador.recomendar("Cidade de Deus")

# Resultado esperado:
# 1. O Poderoso Chefão (0.923)
# 2. Pulp Fiction (0.887)
# 3. Os Suspeitos (0.756)
```

## 🔬 Análise Detalhada de Similaridade

### Comparando Filmes Similares
```python
# Analisar por que dois filmes são similares
recomendador.analisar_similaridade("Matrix", "Interestelar")

# Resultado:
# 🎬 Filme 1: Matrix
#    Gênero: Ação,Ficção
#    Diretor: Wachowski
# 🎬 Filme 2: Interestelar  
#    Gênero: Ficção,Aventura
#    Diretor: Christopher Nolan
# 📊 Similaridade: 0.856
# ✅ Filmes muito similares!
```

### Comparando Filmes Diferentes
```python
# Ver por que filmes são diferentes
recomendador.analisar_similaridade("Matrix", "Toy Story")

# Resultado:
# 📊 Similaridade: 0.123
# ❌ Filmes pouco similares
```

## 📊 Explorando os Dados

### Análise Exploratória Completa
```python
# Ver estatísticas dos dados
recomendador.explorar_dados()

# Resultado:
# 📊 Total de filmes: 22
# 📅 Período: 1972 - 2014
# 🎭 Gêneros únicos encontrados: 12 gêneros
# 🎬 Diretores únicos: 20
```

### Verificar Filmes Disponíveis
```python
# Ver todos os filmes na base
print("Filmes disponíveis:")
for i, filme in enumerate(recomendador.dados['titulo'], 1):
    print(f"{i:2d}. {filme}")
```

## 🧪 Experimentação Avançada

### 1. Testando com Diferentes Números de Recomendações
```python
# Pedir mais ou menos recomendações
recomendacoes_3, _ = recomendador.recomendar("Matrix", 3)
recomendacoes_10, _ = recomendador.recomendar("Matrix", 10)

print(f"Top 3: {len(recomendacoes_3)} filmes")
print(f"Top 10: {len(recomendacoes_10)} filmes")
```

### 2. Analisando Scores de Similaridade
```python
def analisar_scores(filme, num_rec=5):
    """Analisa os scores de similaridade"""
    recomendacoes, scores = recomendador.recomendar(filme, num_rec)
    
    print(f"📊 Análise de similaridade para '{filme}':")
    for titulo, score in zip(recomendacoes, scores):
        if score > 0.8:
            nivel = "🔥 Muito similar"
        elif score > 0.6:
            nivel = "✅ Similar"
        elif score > 0.4:
            nivel = "🔶 Moderadamente similar"
        else:
            nivel = "❌ Pouco similar"
            
        print(f"  {titulo}: {score:.3f} - {nivel}")

# Exemplo de uso
analisar_scores("Matrix")
```

### 3. Comparação Entre Múltiplos Filmes
```python
def comparar_recomendacoes(filmes_base):
    """Compara recomendações de diferentes filmes"""
    print("🔍 Comparação de Recomendações:")
    print("="*50)
    
    for filme in filmes_base:
        print(f"\n🎬 {filme}:")
        recomendacoes, scores = recomendador.recomendar(filme, 3)
        
        for i, (titulo, score) in enumerate(zip(recomendacoes, scores), 1):
            print(f"  {i}. {titulo} ({score:.3f})")

# Exemplo
comparar_recomendacoes(["Matrix", "Toy Story", "O Poderoso Chefão"])
```

## 🎯 Casos de Uso Práticos

### 1. Sistema de Recomendação para Website
```python
class WebRecommendationSystem:
    def __init__(self):
        self.recomendador = RecomendadorFilmes()
        self.recomendador.carregar_dados()
        self.recomendador.treinar_modelo()
    
    def get_recommendations_api(self, movie_title, count=5):
        """API endpoint para recomendações"""
        try:
            recomendacoes, scores = self.recomendador.recomendar(movie_title, count)
            
            return {
                "status": "success",
                "movie": movie_title,
                "recommendations": [
                    {"title": titulo, "similarity": score}
                    for titulo, score in zip(recomendacoes, scores)
                ]
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

# Uso
web_system = WebRecommendationSystem()
result = web_system.get_recommendations_api("Matrix")
print(result)
```

### 2. Análise de Preferências de Usuário
```python
def analisar_preferencias_usuario(filmes_curtidos):
    """Analisa preferências baseado em filmes curtidos"""
    print("🎭 Análise de Preferências do Usuário")
    print("="*40)
    
    todas_recomendacoes = []
    
    for filme in filmes_curtidos:
        print(f"\nBaseado em '{filme}':")
        recomendacoes, scores = recomendador.recomendar(filme, 3)
        
        for titulo, score in zip(recomendacoes, scores):
            todas_recomendacoes.append((titulo, score))
            print(f"  - {titulo} ({score:.3f})")
    
    # Encontrar filmes mais recomendados
    from collections import Counter
    filmes_count = Counter([filme for filme, _ in todas_recomendacoes])
    
    print(f"\n🏆 Filmes mais recomendados para você:")
    for filme, count in filmes_count.most_common(5):
        print(f"  {filme}: recomendado {count}x")

# Exemplo
filmes_usuario = ["Matrix", "Interestelar", "Blade Runner"]
analisar_preferencias_usuario(filmes_usuario)
```

### 3. Descoberta de Filmes por Gênero
```python
def descobrir_por_genero(genero_desejado):
    """Encontra filmes de um gênero específico"""
    filmes_genero = recomendador.dados[
        recomendador.dados['genero'].str.contains(genero_desejado, case=False)
    ]
    
    print(f"🎭 Filmes de {genero_desejado}:")
    for _, filme in filmes_genero.iterrows():
        print(f"  - {filme['titulo']} ({filme['ano']})")
        print(f"    Diretor: {filme['diretor']}")
        print(f"    Gêneros: {filme['genero']}")
        print()

# Exemplos
descobrir_por_genero("Ficção")
descobrir_por_genero("Animação")
descobrir_por_genero("Crime")
```

## 🧮 Entendendo a Matemática

### Visualizando a Matriz TF-IDF
```python
def visualizar_tfidf():
    """Mostra como funciona a vetorização TF-IDF"""
    # Pegar algumas características para exemplo
    caracteristicas = recomendador.dados['caracteristicas'].head(5)
    
    print("📊 Exemplo de Vetorização TF-IDF:")
    print("="*40)
    
    for i, carac in enumerate(caracteristicas):
        print(f"{i+1}. {recomendador.dados.iloc[i]['titulo']}")
        print(f"   Características: {carac}")
        print()

visualizar_tfidf()
```

### Analisando a Matriz de Similaridade
```python
def analisar_matriz_similaridade():
    """Analisa a matriz de similaridade"""
    matriz = recomendador.matriz_similaridade
    
    print("📐 Análise da Matriz de Similaridade:")
    print(f"   Dimensões: {matriz.shape}")
    print(f"   Similaridade máxima: {matriz.max():.3f}")
    print(f"   Similaridade mínima: {matriz.min():.3f}")
    print(f"   Similaridade média: {matriz.mean():.3f}")
    
    # Encontrar o par mais similar (excluindo diagonal)
    np.fill_diagonal(matriz, 0)  # Remove diagonal
    max_idx = np.unravel_index(matriz.argmax(), matriz.shape)
    
    filme1 = recomendador.dados.iloc[max_idx[0]]['titulo']
    filme2 = recomendador.dados.iloc[max_idx[1]]['titulo']
    similaridade = matriz[max_idx]
    
    print(f"\n🏆 Par mais similar:")
    print(f"   {filme1} ↔ {filme2}")
    print(f"   Similaridade: {similaridade:.3f}")

analisar_matriz_similaridade()
```

## 🔧 Personalizações e Melhorias

### 1. Adicionando Novos Filmes
```python
def adicionar_filme(titulo, genero, diretor, ano):
    """Adiciona um novo filme ao sistema"""
    novo_filme = {
        'titulo': titulo,
        'genero': genero,
        'diretor': diretor,
        'ano': ano
    }
    
    # Adicionar ao DataFrame
    recomendador.dados = recomendador.dados.append(novo_filme, ignore_index=True)
    
    # Retreinar o modelo
    recomendador.dados['caracteristicas'] = (
        recomendador.dados['genero'] + ',' + 
        recomendador.dados['diretor']
    )
    recomendador.treinar_modelo()
    
    print(f"✅ Filme '{titulo}' adicionado com sucesso!")

# Exemplo
adicionar_filme("Duna", "Ficção,Aventura", "Denis Villeneuve", 2021)
```

### 2. Salvando e Carregando Modelos
```python
import pickle

def salvar_modelo(nome_arquivo="modelo_recomendacao.pkl"):
    """Salva o modelo treinado"""
    modelo_data = {
        'dados': recomendador.dados,
        'matriz_similaridade': recomendador.matriz_similaridade,
        'indices': recomendador.indices,
        'vectorizer': recomendador.vectorizer
    }
    
    with open(nome_arquivo, 'wb') as f:
        pickle.dump(modelo_data, f)
    
    print(f"💾 Modelo salvo em {nome_arquivo}")

def carregar_modelo(nome_arquivo="modelo_recomendacao.pkl"):
    """Carrega um modelo salvo"""
    with open(nome_arquivo, 'rb') as f:
        modelo_data = pickle.load(f)
    
    recomendador.dados = modelo_data['dados']
    recomendador.matriz_similaridade = modelo_data['matriz_similaridade']
    recomendador.indices = modelo_data['indices']
    recomendador.vectorizer = modelo_data['vectorizer']
    
    print(f"📂 Modelo carregado de {nome_arquivo}")

# Exemplo de uso
salvar_modelo()
# carregar_modelo()
```

## 🎯 Dicas de Performance

1. **Para datasets grandes**: Use `sparse matrices` para economizar memória
2. **Para tempo real**: Pré-calcule recomendações para filmes populares
3. **Para precisão**: Adicione mais features (atores, ano, rating)
4. **Para diversidade**: Implemente re-ranking para evitar recomendações muito similares

## 🚀 Próximos Experimentos

1. Adicione mais filmes ao dataset
2. Experimente com diferentes algoritmos de similaridade
3. Implemente collaborative filtering
4. Crie uma interface web simples
5. Adicione avaliação de usuários como feature