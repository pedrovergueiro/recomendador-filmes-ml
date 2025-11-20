# 🎬 Sistema de Recomendação de Filmes

## 📌 Sobre o Projeto
Sistema de recomendação baseado em conteúdo que sugere filmes similares usando técnicas de Machine Learning.

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **pandas**: Manipulação de dados
- **scikit-learn**: Algoritmos de ML
- **TF-IDF**: Processamento de texto
- **Cosine Similarity**: Cálculo de similaridade

## 🧠 Conceitos de ML Demonstrados

### 1. **Pré-processamento de Dados**
- Combinação de features (gênero + diretor)
- Preparação para o modelo

### 2. **Engenharia de Features**
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Converte texto em vetores numéricos
- Captura a importância das palavras no contexto

### 3. **Algoritmo de Similaridade**
- **Cosine Similarity**: Mede similaridade entre vetores
- Baseado no ângulo entre os vetores, não na magnitude

### 4. **Sistema de Recomendação**
- **Filtragem Baseada em Conteúdo**: Recomenda itens similares
- Não precisa de histórico de usuários

## 🎯 Como Funciona
1. **Treinamento**: Converte características dos filmes em vetores
2. **Similaridade**: Calcula quão similares os filmes são entre si
3. **Recomendação**: Encontra os filmes mais similares ao escolhido

## 📊 Exemplo de Uso