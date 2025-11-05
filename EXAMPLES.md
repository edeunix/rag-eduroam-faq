# 📖 Exemplos de Uso

## Exemplos Básicos

### 1. Executar o Script

```bash
python RAG-eduroam.py
```

### 2. Fazer Perguntas Personalizadas

Você pode modificar a lista de perguntas no final do arquivo `RAG-eduroam.py`:

```python
perguntas = [
    "O que é eduroam?",
    "Como faço meu cadastro?",
    "Onde encontro pontos de acesso?",
    "Como conectar minha instituição?",
    "Sua pergunta aqui"  # Adicione novas perguntas
]
```

## Exemplos de Perguntas Suportadas

### Sobre o Serviço

```python
perguntar("O que é eduroam?")
```

**Resposta esperada:**
> O eduroam (education roaming) é uma iniciativa da Terena para oferecer serviço de acesso a rede sem fio, de forma segura, para a comunidade internacional de educação e pesquisa.

---

### Cadastro de Usuários

```python
perguntar("Como faço meu cadastro para utilizar o eduroam?")
```

**Resposta esperada:**
> A base de usuários do serviço eduroam é gerenciada pelas próprias instituições participantes do serviço. O usuário deve entrar em contato com a própria instituição e solicitar acesso.

---

### Localizar Pontos de Acesso

```python
perguntar("Onde encontro pontos de acesso eduroam?")
```

**Resposta esperada:**
> O mapa dos pontos de acesso podem ser acessados através do APP "eduroam Companion", disponível para Android e IOS.

---

### Conexão de Instituições

```python
perguntar("Como conectar minha instituição no eduroam?")
```

**Resposta esperada:**
> A instituição deve entrar em contato com o atendimento da RNP solicitando a adesão. É indispensável que a instituição já tenha realizado adesão a CAFe e também possua uma infraestrutura de rede sem fio pronta.

---

## Uso Interativo (Python REPL)

```python
# Importar a função
from RAG_eduroam import perguntar

# Fazer perguntas
perguntar("Posso usar portal web para autenticação?")
perguntar("Qual SSID devo usar?")
perguntar("Como ativar eduroam em outros campi?")
```

## Personalização Avançada

### Ajustar Número de Resultados

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}  # Buscar top 5 em vez de 3
)
```

### Modificar Tamanho dos Chunks

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,      # Aumentar para capturar mais contexto
    chunk_overlap=150    # Mais sobreposição
)
```

### Trocar Modelo de Embeddings

```python
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"  # Modelo maior
)
```

## Troubleshooting

### Problema: "No module named 'langchain'"

**Solução:**
```bash
pip install -r requirements.txt
```

### Problema: Respostas Genéricas

**Solução:** Aumentar o número de chunks (`k`) ou o tamanho dos chunks.

### Problema: Modelo Demora para Carregar

**Solução:** Os modelos são baixados apenas na primeira execução. Nas próximas execuções serão mais rápidas.

## Performance

- **Primeira execução:** ~30-60 segundos (download de modelos)
- **Execuções subsequentes:** ~5-10 segundos
- **Cada pergunta:** ~1-2 segundos

## Próximos Passos

1. ✅ Integrar com uma API REST
2. ✅ Adicionar interface web (Streamlit/Gradio)
3. ✅ Suportar múltiplas fontes de dados
4. ✅ Adicionar cache de respostas
5. ✅ Implementar logging

---

**Nota:** Este sistema usa modelos locais e não requer APIs pagas ou chaves de acesso!
