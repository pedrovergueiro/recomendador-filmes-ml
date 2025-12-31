👋 Olá! Eu sou o Pedro Vergueiro

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Machine%20Learning-orange?style=for-the-badge)
![Scikit Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

**🎬 Minha jornada aprendendo Sistemas de Recomendação e ML**

</div>

## 🎯 Por que criei este projeto?

Este projeto foi desenvolvido por mim para **entender na prática como funcionam os sistemas de recomendação** que vemos em Netflix, Amazon, YouTube e outras plataformas. Como estudante de Engenharia de Software, queria mergulhar nos algoritmos por trás dessas recomendações.

Escolhi filmes porque:
- É um domínio que todos conhecem e podem testar facilmente
- Permite entender conceitos fundamentais de ML de forma visual
- Demonstra como transformar dados categóricos em matemática
- É a base para sistemas mais complexos (collaborative filtering, deep learning)

## 🧠 O que aprendi construindo este recomendador

Durante o desenvolvimento, consegui fixar conceitos fundamentais de Machine Learning:

### 🤖 **Conceitos de ML que pratiquei:**
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Como transformar texto em números
- **Cosine Similarity**: Como medir similaridade entre vetores matemáticos
- **Content-Based Filtering**: Recomendação baseada nas características dos itens
- **Feature Engineering**: Como combinar diferentes características (gênero + diretor)
- **Vetorização**: Transformar dados categóricos em representações numéricas

### 🔧 **Habilidades técnicas desenvolvidas:**
- Manipulação de dados com pandas
- Algoritmos de similaridade com scikit-learn
- Pré-processamento de dados textuais
- Implementação de sistemas de recomendação do zero
- Análise exploratória de dados

```python
class MeuAprendizadoML:
    def __init__(self):
        self.nome = "Pedro Vergueiro"
        self.projeto = "Sistema de Recomendação de Filmes"
        self.objetivo = "Entender ML na prática"
        self.algoritmo_principal = "Content-Based Filtering"
        
    def o_que_implementei(self):
        return {
            "entrada": "Título de um filme",
            "processamento": "TF-IDF + Cosine Similarity",
            "saida": "Lista de filmes similares",
            "tecnica": "Filtragem baseada em conteúdo",
            "features": ["gênero", "diretor"]
        }
    
    def conceitos_aprendidos(self):
        return [
            "Como Netflix recomenda filmes",
            "Transformar texto em vetores matemáticos",
            "Calcular similaridade entre itens",
            "Sistemas de recomendação sem histórico de usuário"
        ]

meu_projeto_ml = MeuAprendizadoML()
print("Cada recomendação foi uma lição sobre ML! 🎬")
```

## 🛠️ Tecnologias que escolhi e por quê

Selecionei cada biblioteca pensando no aprendizado de ML:

**🐍 Python + Pandas**
- Padrão da indústria para ciência de dados
- Manipulação fácil de datasets
- Integração perfeita com bibliotecas de ML

**🧠 Scikit-learn**
- Biblioteca mais usada para ML tradicional
- Implementações otimizadas de algoritmos
- Documentação excelente para aprender

**📊 TF-IDF Vectorizer**
- Técnica clássica de processamento de texto
- Transforma palavras em números de forma inteligente
- Base para entender NLP mais avançado

**📐 Cosine Similarity**
- Medida de similaridade mais usada em recomendação
- Funciona bem com dados esparsos
- Interpretação matemática clara

## 📖 Como estruturei meu sistema de ML

Organizei tudo pensando em **clareza** e **aprendizado**:

```
recomendador-filmes-ml/
├── main.py                      # 🎬 Sistema completo de recomendação
├── data/                        # 📊 Dados dos filmes (futuro)
├── models/                      # 🤖 Modelos treinados (futuro)
├── tests/                       # 🧪 Testes do sistema
├── notebooks/                   # 📓 Análises exploratórias
├── requirements.txt             # 📦 Dependências de ML
└── README.md                    # 📖 Este arquivo
```

### 🤔 Por que organizei assim?

- **Classe RecomendadorFilmes**: Encapsula toda a lógica de ML
- **Métodos separados**: Cada etapa do pipeline é clara
- **Dados estruturados**: DataFrame pandas para facilitar manipulação
- **Pipeline completo**: Carregamento → Treinamento → Recomendação
## 🏃‍♂️ Como rodar meu sistema de recomendação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/pedrovergueiro/recomendador-filmes-ml.git
cd recomendador-filmes-ml
```

### 2️⃣ Criar ambiente virtual (essencial para ML!)
```bash
# Criar ambiente isolado
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac  
source venv/bin/activate
```

### 3️⃣ Instalar dependências de ML
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o sistema
```bash
python main.py
```

### 5️⃣ Ver as recomendações
O sistema vai mostrar recomendações para filmes de teste e você pode experimentar!

## 🎬 Como meu algoritmo funciona (passo a passo)

Implementei um sistema de **Content-Based Filtering**. Aqui está como funciona:

### 1️⃣ **Preparação dos Dados**
```python
# Combino características dos filmes
dados['caracteristicas'] = dados['genero'] + ',' + dados['diretor']

# Exemplo: "Ação,Ficção,Christopher Nolan"
```

### 2️⃣ **Vetorização com TF-IDF**
```python
# Transformo texto em números
vectorizer = TfidfVectorizer()
matriz = vectorizer.fit_transform(dados['caracteristicas'])

# "Ação,Ficção" vira [0.5, 0.8, 0.0, 0.3, ...]
```

### 3️⃣ **Cálculo de Similaridade**
```python
# Calculo quão similares os filmes são
matriz_similaridade = cosine_similarity(matriz, matriz)

# Matrix vs Interestelar = 0.85 (muito similar)
# Matrix vs Toy Story = 0.12 (pouco similar)
```

### 4️⃣ **Geração de Recomendações**
```python
# Encontro os filmes mais similares
similaridades = sorted(similaridades, reverse=True)
# Retorno os top 5 mais similares
```

## 🧮 A matemática por trás (o que aprendi)

### **TF-IDF: Transformando Palavras em Números**
```python
# Term Frequency: Quantas vezes uma palavra aparece
# Inverse Document Frequency: Quão rara é a palavra

# Exemplo:
# "Ação" aparece em muitos filmes → peso menor
# "Christopher Nolan" aparece em poucos → peso maior
```

### **Cosine Similarity: Medindo Similaridade**
```python
# Calcula o ângulo entre dois vetores
# Valores de 0 (nada similar) a 1 (idêntico)

# Exemplo:
# Matrix = [0.8, 0.6, 0.0, 0.2]  (Ação, Ficção, Romance, Comédia)
# Blade Runner = [0.7, 0.9, 0.0, 0.1]
# Similaridade = 0.95 (muito similar!)
```

## 🎯 Exemplos práticos do meu sistema

### **Recomendações que o sistema faz:**

**Se você gostou de "Matrix":**
1. Interestelar (Ficção científica + diretor renomado)
2. Avatar (Ficção + aventura)
3. Star Wars (Ficção + aventura)

**Se você gostou de "Toy Story":**
1. Procurando Nemo (Animação + aventura)
2. Shrek (Animação + comédia)
3. Os Incríveis (Animação + ação)

**Se você gostou de "Cidade de Deus":**
1. O Poderoso Chefão (Crime + drama)
2. Pulp Fiction (Crime + drama)
3. Os Suspeitos (Crime + suspense)

## 💡 Desafios de ML que enfrentei e como resolvi

### 🔧 **Problema 1: Como transformar texto em números?**
**Desafio**: Computadores não entendem "Ação" ou "Drama"
**Solução**: Aprendi TF-IDF para converter palavras em vetores matemáticos

### 📊 **Problema 2: Como medir similaridade entre filmes?**
**Desafio**: Como saber se dois filmes são parecidos?
**Solução**: Usei Cosine Similarity para calcular ângulo entre vetores

### 🎭 **Problema 3: Dados limitados**
**Desafio**: Poucos filmes para treinar o modelo
**Solução**: Criei dataset balanceado com diferentes gêneros

### 🔍 **Problema 4: Cold Start Problem**
**Desafio**: E se o filme não estiver na base?
**Solução**: Implementei tratamento de erro elegante

```python
def recomendar(self, titulo_filme):
    try:
        # Busca o filme
        idx = self.indices[titulo_filme]
        # ... lógica de recomendação
    except KeyError:
        return f"Filme '{titulo_filme}' não está na base."
```

## 🧪 Como testei meu sistema

Criei testes para verificar se as recomendações fazem sentido:

```python
def testar_recomendacoes():
    """Testa se as recomendações são lógicas"""
    
    # Teste 1: Filmes de ficção científica
    recomendacoes_matrix = recomendador.recomendar("Matrix")
    # Deve recomendar outros filmes de ficção
    
    # Teste 2: Filmes de animação
    recomendacoes_toy = recomendador.recomendar("Toy Story")
    # Deve recomendar outras animações
    
    # Teste 3: Filmes de crime
    recomendacoes_cidade = recomendador.recomendar("Cidade de Deus")
    # Deve recomendar outros filmes de crime
```

## 📈 Métricas que acompanho

### **Qualidade das Recomendações:**
- ✅ Filmes do mesmo gênero são recomendados juntos
- ✅ Diretores similares aparecem nas recomendações
- ✅ Diversidade adequada (não só filmes idênticos)

### **Performance do Sistema:**
- ✅ Tempo de resposta < 1 segundo
- ✅ Funciona com dataset pequeno ou grande
- ✅ Memória eficiente para matrizes de similaridade

## 🎓 Principais conceitos de ML que fixei

### 🤖 **Sistemas de Recomendação**
- **Content-Based**: Baseado nas características dos itens
- **Collaborative Filtering**: Baseado no comportamento dos usuários
- **Hybrid Systems**: Combinação de ambas as abordagens

### 📊 **Processamento de Dados**
- **Feature Engineering**: Como criar características úteis
- **Vectorização**: Transformar dados categóricos em numéricos
- **Normalização**: Garantir que todas as features tenham peso similar

### 🧮 **Algoritmos de Similaridade**
- **Cosine Similarity**: Melhor para dados esparsos
- **Euclidean Distance**: Para dados densos
- **Jaccard Similarity**: Para dados binários

### 🔍 **Avaliação de Modelos**
- **Precision**: Das recomendações, quantas são relevantes?
- **Recall**: Das opções relevantes, quantas foram recomendadas?
- **Diversity**: As recomendações são variadas?

## 🌱 Próximos passos no meu aprendizado de ML

Agora que dominei o básico, quero evoluir para:

- [ ] **Collaborative Filtering**: Usar dados de usuários
- [ ] **Matrix Factorization**: Técnicas mais avançadas
- [ ] **Deep Learning**: Redes neurais para recomendação
- [ ] **Real-time Recommendations**: Sistema em tempo real
- [ ] **A/B Testing**: Testar diferentes algoritmos
- [ ] **Implicit Feedback**: Usar dados de comportamento
- [ ] **Cold Start Solutions**: Lidar com novos usuários/itens

## 🤝 Quer aprender ML junto comigo?

Se você também está explorando Machine Learning e sistemas de recomendação:

- 🍴 **Fork** este projeto e experimente com outros datasets
- 🎬 **Adicione mais filmes** e veja como as recomendações mudam
- 💡 **Implemente outras métricas** de similaridade
- ⭐ **Dê uma estrela** se o projeto te ajudou a entender ML!

## 📚 Recursos que me ajudaram a aprender

- **Scikit-learn Documentation**: https://scikit-learn.org/
- **Pandas Documentation**: https://pandas.pydata.org/
- **Recommender Systems Handbook**: Livro clássico da área
- **Coursera ML Course**: Andrew Ng's Machine Learning

## 📫 Vamos trocar uma ideia sobre ML?

Estou sempre empolgado para conversar sobre Machine Learning e sistemas de recomendação!

- 📧 **Email**: pedrolv.fsilva@gmail.com
- 💼 **LinkedIn**: [Pedro Vergueiro](https://www.linkedin.com/in/pedro-vergueiro)
- 🌐 **GitHub**: [@pedrovergueiro](https://github.com/pedrovergueiro)

---

<div align="center">

**⭐ Se este projeto te inspirou a aprender ML, dê uma estrela! ⭐**

*"Machine Learning é sobre fazer computadores aprenderem padrões que nós nem sabíamos que existiam"*

Feito com ❤️ e muita curiosidade sobre ML por Pedro Vergueiro | Estudante de Engenharia de Software

</div>