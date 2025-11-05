#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema RAG (Retrieval Augmented Generation) para FAQ do eduroam
Versão simples e funcional - retorna respostas diretas
"""

import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

print("🚀 Iniciando sistema RAG eduroam...\n")

# 1. Scraping da página
url = "https://ajuda.rnp.br/eduroam/perguntas-frequentes"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text_content = soup.get_text(separator='\n', strip=True)

# 2. Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100
)
chunks = text_splitter.split_text(text_content)

# 3. Criar embeddings e vector store
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db_final"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

print("✅ Sistema carregado!\n")
print("=" * 80)

def perguntar(pergunta):
    """Faz uma pergunta e retorna a melhor resposta encontrada"""
    print(f"\n🔍 PERGUNTA: {pergunta}")
    print("-" * 80)
    
    docs = retriever.invoke(pergunta)
    
    if not docs:
        print("❌ Nenhuma informação encontrada.\n")
        return
    
    # Pegar o documento mais relevante e limpar
    melhor_resposta = docs[0].page_content
    
    # Encontrar a parte relevante (depois da pergunta se existir)
    linhas = melhor_resposta.split('\n')
    resposta_limpa = []
    
    for i, linha in enumerate(linhas):
        linha = linha.strip()
        if not linha:
            continue
        
        # Se encontrar a pergunta específica ou similar
        if pergunta.lower() in linha.lower() or \
           any(palavra in linha.lower() for palavra in pergunta.lower().split() if len(palavra) > 4):
            # Pegar as próximas linhas como resposta
            for j in range(i+1, min(i+5, len(linhas))):
                if linhas[j].strip() and not linhas[j].strip().startswith(('http', 'Was this', 'Copy', 'Powered')):
                    resposta_limpa.append(linhas[j].strip())
            if resposta_limpa:
                break
    
    # Se não encontrou dessa forma, mostrar o trecho completo
    if not resposta_limpa:
        # Filtrar linhas de menu/navegação
        for linha in linhas:
            linha = linha.strip()
            if linha and len(linha) > 20 and \
               not any(skip in linha for skip in ['Ctrl', 'GitBook', 'Was this', 'Copy', 'More', 'On this page']):
                resposta_limpa.append(linha)
                if len(resposta_limpa) >= 3:
                    break
    
    print("💡 RESPOSTA:")
    print()
    if resposta_limpa:
        for linha in resposta_limpa[:5]:  # Limitar a 5 linhas
            print(f"   {linha}")
    else:
        print(f"   {melhor_resposta[:500]}...")
    
    print()
    print("-" * 80)

# Exemplos de uso
perguntas = [
    "O que é eduroam?",
    "Como faço meu cadastro?",
    "Onde encontro pontos de acesso?",
    "Como conectar minha instituição?"
]

for pergunta in perguntas:
    perguntar(pergunta)

print("\n" + "=" * 80)
print("✅ Demonstração concluída!")
print("\nPara fazer mais perguntas, use: perguntar('sua pergunta aqui')")
