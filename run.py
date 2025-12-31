#!/usr/bin/env python3
"""
🚀 Script para rodar o Sistema de Recomendação de Filmes

Execute este arquivo para iniciar o sistema de ML.
Comando: python run.py

Autor: Pedro Vergueiro
Projeto: Sistema de Recomendação com Machine Learning
"""

import sys
import os
from main import main as executar_sistema

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    try:
        import pandas
        import numpy
        import sklearn
        print("✅ Dependências de ML encontradas")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("💡 Execute: pip install -r requirements.txt")
        return False

def mostrar_info():
    """Mostra informações sobre o sistema"""
    print("🎬" + "="*59)
    print("🎬 SISTEMA DE RECOMENDAÇÃO DE FILMES - PEDRO VERGUEIRO")
    print("🎬" + "="*59)
    print("🤖 Usando Machine Learning para recomendar filmes!")
    print("📚 Técnicas: TF-IDF + Cosine Similarity + Content-Based Filtering")
    print("🎯 Objetivo: Aprender sistemas de recomendação na prática")
    print()

def main():
    """Função principal para iniciar o sistema"""
    mostrar_info()
    
    # Verificar dependências
    if not check_dependencies():
        sys.exit(1)
    
    print("🔄 Iniciando sistema de recomendação...")
    print("⏳ Carregando dados e treinando modelo de ML...")
    print()
    
    try:
        # Executar o sistema principal
        executar_sistema()
        
        print("\n" + "="*60)
        print("🎉 Sistema executado com sucesso!")
        print("💡 Dicas para experimentar:")
        print("   - Modifique os filmes no dataset (main.py)")
        print("   - Teste com diferentes números de recomendações")
        print("   - Analise a similaridade entre filmes específicos")
        print("   - Execute os testes: pytest test_recomendador.py -v")
        
    except KeyboardInterrupt:
        print("\n🛑 Sistema interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao executar sistema: {e}")
        print("🔧 Verifique se todas as dependências estão instaladas")
        sys.exit(1)

if __name__ == "__main__":
    main()