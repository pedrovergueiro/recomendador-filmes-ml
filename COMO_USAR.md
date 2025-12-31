# 🚀 Como Usar o Sistema de Recomendação de Filmes

## ✅ Guia Rápido

Este sistema usa **Machine Learning** para recomendar filmes similares baseado em gênero e diretor. É perfeito para aprender sobre sistemas de recomendação!

### 🏃‍♂️ Para Rodar o Sistema

```bash
# 1. Clone o repositório
git clone https://github.com/pedrovergueiro/recomendador-filmes-ml.git
cd recomendador-filmes-ml

# 2. Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute o sistema
python main.py
```

### 🎬 Ver as Recomendações

O sistema vai mostrar recomendações automáticas para filmes de teste e análises detalhadas!

## 🤖 Como o Sistema Funciona

### **Entrada**: Nome de um filme
```
"Matrix"
```

### **Processamento**: Machine Learning
1. **TF-IDF**: Transforma características em números
2. **Cosine Similarity**: Calcula similaridade entre filmes
3. **Ranking**: Ordena por relevância

### **Saída**: Lista de filmes similares
```
1. Interestelar (0.856)
2. Avatar (0.743)
3. Star Wars (0.721)
```

## 📊 Filmes Disponíveis no Sistema

O sistema atual tem **22 filmes** de diferentes gêneros:

### 🎭 **Por Gênero:**
- **Ficção Científica**: Matrix, Interestelar, Avatar, Star Wars, Blade Runner
- **Animação**: Toy Story, Procurando Nemo, Shrek, Os Incríveis
- **Crime/Drama**: O Poderoso Chefão, Pulp Fiction, Cidade de Deus
- **Aventura**: O Senhor dos Anéis, Harry Potter
- **Ação**: Vingadores, Gladiador, Terminator

### 🎬 **Por Diretor:**
- **Christopher Nolan**: Interestelar
- **Ridley Scott**: Gladiador, Blade Runner, Alien
- **James Cameron**: Avatar, Terminator
- **Quentin Tarantino**: Pulp Fiction

## 🧪 Testando o Sistema

### **Teste Básico**
```python
from main import RecomendadorFilmes

# Inicializar
recomendador = RecomendadorFilmes()
recomendador.carregar_dados()
recomendador.treinar_modelo()

# Fazer recomendação
recomendacoes, scores = recomendador.recomendar("Matrix")
print(recomendacoes)
```

### **Teste com Análise**
```python
# Ver por que filmes são similares
recomendador.analisar_similaridade("Matrix", "Interestelar")
```

## 📈 Interpretando os Resultados

### **Scores de Similaridade:**
- **0.8 - 1.0**: Muito similares (mesmo gênero + características)
- **0.6 - 0.8**: Similares (gênero parecido)
- **0.4 - 0.6**: Moderadamente similares
- **0.0 - 0.4**: Pouco similares

### **Exemplo de Interpretação:**
```
Matrix → Interestelar (0.856)
Por quê? Ambos são ficção científica com diretores renomados
```

## 🔧 Personalizando o Sistema

### **1. Adicionar Novos Filmes**
Edite o arquivo `main.py` na função `carregar_dados()`:

```python
filmes = {
    'titulo': [..., 'Seu Novo Filme'],
    'genero': [..., 'Gênero,Subgênero'],
    'diretor': [..., 'Nome do Diretor'],
    'ano': [..., 2024]
}
```

### **2. Mudar Número de Recomendações**
```python
# Pedir mais recomendações
recomendacoes = recomendador.recomendar("Matrix", 10)
```

### **3. Testar com Seus Filmes Favoritos**
```python
meus_filmes = ["Matrix", "Toy Story", "O Poderoso Chefão"]

for filme in meus_filmes:
    print(f"Se você gostou de {filme}:")
    recomendacoes, _ = recomendador.recomendar(filme)
    print(recomendacoes)
```

## 🧠 Conceitos de ML que Você Vai Aprender

### **1. TF-IDF (Term Frequency-Inverse Document Frequency)**
- Transforma texto em números
- Palavras raras têm mais peso
- Base para processamento de linguagem natural

### **2. Cosine Similarity**
- Mede ângulo entre vetores
- Ignora magnitude, foca na direção
- Perfeito para dados esparsos

### **3. Content-Based Filtering**
- Recomenda baseado nas características dos itens
- Não precisa de dados de usuários
- Funciona bem para novos itens

### **4. Feature Engineering**
- Combinar diferentes características
- Criar representações úteis dos dados
- Fundamental para ML eficaz

## 🎯 Casos de Uso Práticos

### **1. Sistema de Streaming**
```python
# Usuário assistiu Matrix
filme_assistido = "Matrix"
recomendacoes, _ = recomendador.recomendar(filme_assistido)
print(f"Baseado em {filme_assistido}, recomendamos:")
for filme in recomendacoes:
    print(f"- {filme}")
```

### **2. Análise de Preferências**
```python
# Analisar padrão de gostos
filmes_curtidos = ["Matrix", "Interestelar", "Blade Runner"]
print("Você parece gostar de ficção científica!")
```

### **3. Descoberta de Novos Gêneros**
```python
# Expandir horizontes
filme_conhecido = "Toy Story"
recomendacoes, _ = recomendador.recomendar(filme_conhecido)
print("Se você gosta de animação, pode gostar de:")
print(recomendacoes)
```

## 🐛 Problemas Comuns

### **Filme não encontrado**
```
❌ Filme 'Titanic' não está na base de dados.
```
**Solução**: Adicione o filme ao dataset ou use um filme da lista disponível.

### **Recomendações estranhas**
**Causa**: Dataset pequeno ou características limitadas
**Solução**: Adicione mais filmes e características (atores, ano, rating)

### **Todas as recomendações são muito similares**
**Causa**: Features muito específicas
**Solução**: Adicione diversidade no re-ranking

## 📚 Recursos para Aprender Mais

### **Documentação das Bibliotecas:**
- **Pandas**: https://pandas.pydata.org/docs/
- **Scikit-learn**: https://scikit-learn.org/stable/
- **NumPy**: https://numpy.org/doc/

### **Conceitos de ML:**
- **TF-IDF**: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- **Cosine Similarity**: https://en.wikipedia.org/wiki/Cosine_similarity
- **Recommender Systems**: Livro "Recommender Systems Handbook"

### **Cursos Recomendados:**
- **Machine Learning (Coursera)**: Andrew Ng
- **Recommender Systems (Coursera)**: University of Minnesota
- **Python for Data Science**: DataCamp

## 🚀 Próximos Passos

1. **Execute o sistema** e veja as recomendações
2. **Teste com diferentes filmes** da lista disponível
3. **Adicione seus filmes favoritos** ao dataset
4. **Experimente modificar** os algoritmos
5. **Implemente melhorias** como interface web

## 💡 Dicas de Experimentação

1. **Comece simples**: Use o sistema como está
2. **Entenda os resultados**: Por que certas recomendações fazem sentido?
3. **Modifique gradualmente**: Adicione filmes, mude parâmetros
4. **Compare algoritmos**: Teste diferentes métricas de similaridade
5. **Documente descobertas**: Anote o que funciona melhor

---

**Criado por Pedro Vergueiro** - Projeto de aprendizado sobre Machine Learning e Sistemas de Recomendação 🎬🤖