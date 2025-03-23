# 🤖 Chatbot de Logística (Usando Google Gemini)

Este projeto é um chatbot desenvolvido em Python que responde perguntas sobre **logística** utilizando a API **Gemini (Google AI)**.
O chatbot permite que o usuário faça **três perguntas** e, ao final, gera um **resumo** das respostas fornecidas.

---

## 📌 **Funcionalidades**
✅ Responde até **três perguntas** do usuário sobre logística.  
✅ Utiliza **IA Generativa** para fornecer respostas precisas.  
✅ Exibe um **resumo final** com todas as perguntas e respostas.  
✅ Desenvolvido em **Python** com suporte a **.env** para segurança da API.  

---

## 🛠 **Tecnologias utilizadas**
- **Python 3.10+**
- **Google Generative AI (Gemini)**
- **Bibliotecas:**
  - `google-generativeai` (para interagir com a API do Gemini)
  - `python-dotenv` (para gerenciar variáveis de ambiente)

---

## 🚀 **Como executar o projeto**


```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate  # Para Windows
```

### 3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4️⃣ Crie um arquivo `.env` com sua chave da API do Google Gemini:
```env
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXX
```

### 5️⃣ Execute o chatbot:
```bash
python main.py
```

---

## 📜 **Exemplo de uso**
```bash
🤖 Bem-vindo ao Chatbot de Logística (Powered by Gemini)!
Você pode fazer até 3 perguntas sobre logística.

Digite sua 1ª pergunta: Qual a capacidade de carga de um caminhão bitrem?

Resposta: O caminhão bitrem pode transportar cargas de até 57 toneladas, dependendo das regulamentações locais e do tipo de carga.

--------------------------------------------------

📋 RESUMO DAS RESPOSTAS:
1. Pergunta: Qual a capacidade de carga de um caminhão bitrem?
   Resposta: O caminhão bitrem pode transportar cargas de até 57 toneladas...
```

---

## 📦 **Estrutura do projeto**
```
chatbot-logistica/
│
├── main.py                # Arquivo principal do chatbot
├── .env                   # Chave da API (Não deve ser commitado)
├── .gitignore             # Para ignorar arquivos sensíveis
├── requirements.txt       # Lista de dependências
├── README.md              # Documentação do projeto
└── venv/                  # Ambiente virtual (opcional)
```

---

## 🔥 **Possíveis problemas e soluções**
### ❌ ERRO: "A chave da API do Gemini não foi encontrada"
✅ **Solução:** Verifique se o arquivo `.env` foi criado e se a chave `GEMINI_API_KEY` está correta.

### ❌ ERRO: "Método não suportado na API"
✅ **Solução:** Atualize a biblioteca `google-generativeai` com:
```bash
pip install --upgrade google-generativeai
```

---

## 🎥 **Demonstração em vídeo**
[![Assista no YouTube](https://img.youtube.com/vi/SEU_VIDEO_ID/maxresdefault.jpg)](https://youtu.be/SEU_VIDEO_ID)

---


---


### .\venv\Scripts\Activate

