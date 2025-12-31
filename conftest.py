"""
Configuração do pytest para testes do sistema de recomendação

Este arquivo configura o ambiente de testes para o sistema de ML.
"""
import sys
import os

# Adicionar o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))