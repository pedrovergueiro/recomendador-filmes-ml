"""
🧪 Testes do Sistema de Recomendação de Filmes

Aqui testo se meu sistema de ML está funcionando corretamente.
Testar sistemas de ML é diferente de testar código normal!

O que aprendi sobre testes de ML:
- Resultados podem variar, então testo estrutura e lógica
- Importante testar casos extremos (filme não encontrado)
- Validar se as recomendações fazem sentido logicamente
- Testar performance com diferentes tamanhos de dados
"""

import pytest
import pandas as pd
import numpy as np
from main import RecomendadorFilmes

class TestRecomendadorFilmes:
    """
    Classe de testes para o sistema de recomendação.
    
    Testa todas as funcionalidades principais do sistema.
    """
    
    @pytest.fixture
    def recomendador(self):
        """
        Fixture que cria um sistema treinado para os testes.
        
        Fixture é uma função que prepara dados para os testes.
        """
        sistema = RecomendadorFilmes()
        sistema.carregar_dados()
        sistema.treinar_modelo()
        return sistema
    
    def test_carregar_dados(self, recomendador):
        """
        🔍 Testa se os dados são carregados corretamente
        """
        # Verificar se os dados foram carregados
        assert recomendador.dados is not None
        assert len(recomendador.dados) > 0
        
        # Verificar se as colunas necessárias existem
        colunas_esperadas = ['titulo', 'genero', 'diretor', 'ano', 'caracteristicas']
        for coluna in colunas_esperadas:
            assert coluna in recomendador.dados.columns
        
        # Verificar se não há valores nulos nas colunas importantes
        assert not recomendador.dados['titulo'].isnull().any()
        assert not recomendador.dados['caracteristicas'].isnull().any()
        
        print(f"✅ Dados carregados: {len(recomendador.dados)} filmes")
    
    def test_treinar_modelo(self, recomendador):
        """
        🤖 Testa se o modelo é treinado corretamente
        """
        # Verificar se a matriz de similaridade foi criada
        assert recomendador.matriz_similaridade is not None
        
        # Verificar dimensões da matriz
        num_filmes = len(recomendador.dados)
        assert recomendador.matriz_similaridade.shape == (num_filmes, num_filmes)
        
        # Verificar se a matriz é simétrica (similaridade A->B = B->A)
        assert np.allclose(
            recomendador.matriz_similaridade, 
            recomendador.matriz_similaridade.T
        )
        
        # Verificar se a diagonal é 1 (filme é idêntico a si mesmo)
        diagonal = np.diag(recomendador.matriz_similaridade)
        assert np.allclose(diagonal, 1.0)
        
        # Verificar se os índices foram criados
        assert recomendador.indices is not None
        assert len(recomendador.indices) > 0
        
        print("✅ Modelo treinado corretamente")
    
    def test_recomendar_filme_existente(self, recomendador):
        """
        🎬 Testa recomendações para filme que existe na base
        """
        filme_teste = "Matrix"
        
        # Fazer recomendação
        resultado = recomendador.recomendar(filme_teste, 3)
        
        # Verificar se retornou tupla (recomendacoes, scores)
        assert isinstance(resultado, tuple)
        assert len(resultado) == 2
        
        recomendacoes, scores = resultado
        
        # Verificar se retornou pandas Series
        assert isinstance(recomendacoes, pd.Series)
        assert isinstance(scores, list)
        
        # Verificar se retornou o número correto de recomendações
        assert len(recomendacoes) == 3
        assert len(scores) == 3
        
        # Verificar se os scores estão no range correto (0-1)
        for score in scores:
            assert 0 <= score <= 1
        
        # Verificar se os scores estão ordenados (maior primeiro)
        assert scores == sorted(scores, reverse=True)
        
        # Verificar se não recomendou o próprio filme
        assert filme_teste not in recomendacoes.values
        
        print(f"✅ Recomendações para '{filme_teste}': {list(recomendacoes)}")
    
    def test_recomendar_filme_inexistente(self, recomendador):
        """
        ❌ Testa recomendação para filme que não existe
        """
        filme_inexistente = "Filme Que Não Existe"
        
        resultado = recomendador.recomendar(filme_inexistente)
        
        # Deve retornar mensagem de erro
        assert isinstance(resultado, tuple)
        mensagem, scores = resultado
        assert isinstance(mensagem, str)
        assert "não está na base" in mensagem
        assert scores is None
        
        print(f"✅ Tratamento de erro funcionando: {mensagem}")
    
    def test_recomendacoes_fazem_sentido(self, recomendador):
        """
        🧠 Testa se as recomendações fazem sentido logicamente
        """
        # Teste 1: Filmes de ficção científica
        recomendacoes_matrix, scores = recomendador.recomendar("Matrix", 5)
        
        # Verificar se pelo menos um filme de ficção foi recomendado
        filmes_ficcao = ["Interestelar", "Avatar", "Star Wars", "Blade Runner"]
        recomendacoes_list = list(recomendacoes_matrix)
        
        tem_ficcao = any(filme in recomendacoes_list for filme in filmes_ficcao)
        assert tem_ficcao, "Deveria recomendar pelo menos um filme de ficção"
        
        # Teste 2: Filmes de animação
        recomendacoes_toy, _ = recomendador.recomendar("Toy Story", 3)
        filmes_animacao = ["Procurando Nemo", "Shrek", "Os Incríveis"]
        recomendacoes_toy_list = list(recomendacoes_toy)
        
        tem_animacao = any(filme in recomendacoes_toy_list for filme in filmes_animacao)
        assert tem_animacao, "Deveria recomendar pelo menos um filme de animação"
        
        print("✅ Recomendações fazem sentido logicamente")
    
    def test_diferentes_numeros_recomendacoes(self, recomendador):
        """
        🔢 Testa diferentes números de recomendações
        """
        filme = "Matrix"
        
        # Testar diferentes números
        for num in [1, 3, 5, 10]:
            recomendacoes, scores = recomendador.recomendar(filme, num)
            
            # Não pode recomendar mais filmes do que existem na base
            max_possivel = len(recomendador.dados) - 1  # -1 porque exclui o próprio filme
            esperado = min(num, max_possivel)
            
            assert len(recomendacoes) == esperado
            assert len(scores) == esperado
        
        print("✅ Diferentes números de recomendações funcionando")
    
    def test_analisar_similaridade(self, recomendador):
        """
        🔬 Testa análise de similaridade entre filmes
        """
        # Testar com filmes que existem
        try:
            recomendador.analisar_similaridade("Matrix", "Interestelar")
            # Se chegou aqui, não deu erro
            assert True
        except Exception as e:
            pytest.fail(f"Análise de similaridade falhou: {e}")
        
        print("✅ Análise de similaridade funcionando")
    
    def test_explorar_dados(self, recomendador):
        """
        📊 Testa exploração de dados
        """
        # Verificar se a função roda sem erro
        try:
            recomendador.explorar_dados()
            assert True
        except Exception as e:
            pytest.fail(f"Exploração de dados falhou: {e}")
        
        print("✅ Exploração de dados funcionando")
    
    def test_consistencia_recomendacoes(self, recomendador):
        """
        🔄 Testa se as recomendações são consistentes
        """
        filme = "Matrix"
        
        # Fazer a mesma recomendação várias vezes
        recomendacoes1, scores1 = recomendador.recomendar(filme, 5)
        recomendacoes2, scores2 = recomendador.recomendar(filme, 5)
        
        # Devem ser idênticas (modelo determinístico)
        assert list(recomendacoes1) == list(recomendacoes2)
        assert scores1 == scores2
        
        print("✅ Recomendações são consistentes")
    
    def test_matriz_similaridade_propriedades(self, recomendador):
        """
        📐 Testa propriedades matemáticas da matriz de similaridade
        """
        matriz = recomendador.matriz_similaridade
        
        # Teste 1: Valores no range [0, 1] (com tolerância para precisão de ponto flutuante)
        assert np.all(matriz >= 0)
        assert np.all(matriz <= 1.0001)  # Pequena tolerância para erros de precisão
        
        # Teste 2: Diagonal deve ser 1 (filme similar a si mesmo)
        diagonal = np.diag(matriz)
        assert np.allclose(diagonal, 1.0)
        
        # Teste 3: Matriz deve ser simétrica
        assert np.allclose(matriz, matriz.T)
        
        # Teste 4: Não deve ter NaN ou infinitos
        assert not np.any(np.isnan(matriz))
        assert not np.any(np.isinf(matriz))
        
        print("✅ Matriz de similaridade tem propriedades corretas")
    
    def test_performance_basica(self, recomendador):
        """
        ⚡ Testa performance básica do sistema
        """
        import time
        
        filme = "Matrix"
        
        # Medir tempo de recomendação
        start_time = time.time()
        recomendacoes, scores = recomendador.recomendar(filme, 5)
        end_time = time.time()
        
        tempo_execucao = end_time - start_time
        
        # Deve ser rápido (menos de 1 segundo para dataset pequeno)
        assert tempo_execucao < 1.0, f"Muito lento: {tempo_execucao:.3f}s"
        
        print(f"✅ Performance OK: {tempo_execucao:.3f}s para recomendação")

def test_sistema_completo():
    """
    🎬 Teste de integração completa do sistema
    """
    print("\n🎬 Testando sistema completo...")
    
    # Criar e treinar sistema
    recomendador = RecomendadorFilmes()
    recomendador.carregar_dados()
    recomendador.treinar_modelo()
    
    # Testar com diferentes tipos de filmes
    filmes_teste = [
        ("Matrix", "ficção científica"),
        ("Toy Story", "animação"),
        ("O Poderoso Chefão", "crime/drama")
    ]
    
    for filme, categoria in filmes_teste:
        print(f"\n🎯 Testando {categoria}: {filme}")
        
        recomendacoes, scores = recomendador.recomendar(filme, 3)
        
        assert len(recomendacoes) == 3
        assert all(0 <= score <= 1 for score in scores)
        
        print(f"   Recomendações: {list(recomendacoes)}")
        print(f"   Scores: {[f'{s:.3f}' for s in scores]}")
    
    print("\n✅ Sistema completo funcionando perfeitamente!")

if __name__ == "__main__":
    # Executar teste completo se rodado diretamente
    test_sistema_completo()
    
    print("\n🧪 Para rodar todos os testes:")
    print("   pytest test_recomendador.py -v")
    print("\n🔍 Para rodar teste específico:")
    print("   pytest test_recomendador.py::TestRecomendadorFilmes::test_recomendar_filme_existente -v")