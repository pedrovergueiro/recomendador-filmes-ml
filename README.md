# Recomendador de Filmes

Projeto que fiz pra entender como sistemas de recomendação funcionam por dentro. Usei filtragem baseada em conteúdo: o sistema pega as características de um filme (gênero, diretor, elenco, sinopse) e encontra os mais parecidos usando TF-IDF e similaridade por cosseno.

Não é o algoritmo do Netflix. Mas construir do zero me fez entender por que o algoritmo do Netflix é do jeito que é — e quais os limites de cada abordagem.

```python
from main import recomendar

filmes = recomendar("Interestelar", n=5)
# ['Gravity', 'The Martian', 'Contact', ...]
```

## Stack
Python · Scikit-learn · Pandas · NumPy
