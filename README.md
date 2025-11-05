# 🎓 RAG eduroam FAQ - Sistema de Perguntas e Respostas

Sistema de **RAG (Retrieval Augmented Generation)** para responder perguntas sobre o serviço eduroam da RNP, utilizando técnicas de busca semântica e processamento de linguagem natural.

## 📋 Sobre o Projeto

Este projeto implementa um assistente inteligente que:
- 🔍 Faz scraping da [página de FAQ oficial do eduroam](https://ajuda.rnp.br/eduroam/perguntas-frequentes)
- 📚 Cria uma base de conhecimento vetorial usando embeddings multilíngues
- 🤖 Responde perguntas de forma precisa utilizando busca semântica
- ⚡ Funciona 100% localmente, sem necessidade de APIs externas

## 🚀 Funcionalidades

- **Busca Semântica**: Encontra respostas mesmo quando a pergunta usa palavras diferentes
- **Respostas Diretas**: Extrai e apresenta apenas a informação relevante
- **Processamento Local**: Todos os modelos rodam na sua máquina
- **Multilíngue**: Suporta embeddings em português com alta qualidade

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **LangChain**: Framework para aplicações com LLM
- **ChromaDB**: Banco de dados vetorial
- **Sentence Transformers**: Modelos de embeddings multilíngues
- **BeautifulSoup**: Web scraping
- **HuggingFace**: Modelos pré-treinados

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/rag-eduroam-faq.git
cd rag-eduroam-faq
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 🎯 Uso

### Execução Básica

```bash
python RAG-eduroam.py
```

### Exemplo de Saída

```
🚀 Iniciando sistema RAG eduroam...

✅ Sistema carregado!

================================================================================

🔍 PERGUNTA: O que é eduroam?
--------------------------------------------------------------------------------
💡 RESPOSTA:

   O eduroam (education roaming) é uma iniciativa da Terena (Trans-European 
   Research and Education Networking Association), hoje GÉANT, para oferecer 
   serviço de acesso a rede sem fio, de forma segura, para a comunidade 
   internacional de educação e pesquisa. O eduroam está disponível em mais 
   de 100 países, sendo a RNP (Rede Nacional de Ensino e Pesquisa) 
   licenciada a operar o serviço no Brasil.

--------------------------------------------------------------------------------
```

### Uso Programático

```python
from RAG_eduroam import perguntar

# Fazer uma pergunta personalizada
perguntar("Como faço para me conectar ao eduroam?")
perguntar("Quais são os requisitos para instituições?")
```

## 📊 Como Funciona

```
┌─────────────────┐
│  Página Web FAQ │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Web Scraping   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Splitting  │
│   (Chunking)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embeddings    │
│  (Vetorização)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   ChromaDB      │
│ (Vector Store)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Retriever     │
│ (Busca por      │
│  Similaridade)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Resposta     │
│    Formatada    │
└─────────────────┘
```

## 🔧 Configuração Avançada

### Ajustar Tamanho dos Chunks

No arquivo `RAG-eduroam.py`, linha 23-26:

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,      # Tamanho de cada chunk
    chunk_overlap=100    # Sobreposição entre chunks
)
```

### Modificar Número de Resultados

Linha 38:

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # Top 3 resultados
```

## 📁 Estrutura do Projeto

```
rag-eduroam-faq/
├── RAG-eduroam.py          # Script principal
├── requirements.txt        # Dependências
├── README.md              # Este arquivo
├── .gitignore            # Arquivos ignorados pelo Git
└── chroma_db_final/      # Banco vetorial (gerado em runtime)
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Exemplos de Perguntas

O sistema pode responder perguntas como:

- ✅ O que é eduroam?
- ✅ Como faço meu cadastro?
- ✅ Onde encontro pontos de acesso?
- ✅ Como conectar minha instituição?
- ✅ Posso usar portal web para autenticação?
- ✅ Qual o SSID correto?

## ⚠️ Limitações

- A qualidade das respostas depende do conteúdo disponível na página FAQ
- Perguntas muito específicas ou fora do escopo podem não ter resposta
- Requer conexão com internet apenas na primeira execução (para download dos modelos)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Edelberto**

## 🙏 Agradecimentos

- [RNP](https://www.rnp.br/) - Pela documentação do eduroam
- [LangChain](https://www.langchain.com/) - Framework RAG
- [HuggingFace](https://huggingface.co/) - Modelos de embeddings
- Comunidade open-source

## 🔗 Links Úteis

- [Documentação Oficial eduroam RNP](https://ajuda.rnp.br/eduroam)
- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
