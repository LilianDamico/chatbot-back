import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura a chave da API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️ ERRO: A chave da API do Gemini não foi encontrada. Verifique o arquivo .env.")
    exit(1)

genai.configure(api_key=api_key)

# Inicializa o modelo Gemini
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def responder_pergunta(pergunta):
    """Envia a pergunta para o Gemini e retorna a resposta."""
    try:
        resposta = model.generate_content(pergunta)
        return resposta.text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

def main():
    print("🤖 Bem-vindo ao Chatbot de Logística (Powered by Gemini)!")
    print("Você pode fazer até 3 perguntas sobre logística.\n")

    perguntas = []
    respostas = []

    for i in range(3):
        pergunta = input(f"Digite sua {i+1}ª pergunta: ")
        resposta = responder_pergunta(pergunta)
        perguntas.append(pergunta)
        respostas.append(resposta)

        print(f"\nResposta: {resposta}\n{'-'*50}")

    print("\n📋 RESUMO DAS RESPOSTAS:")
    for i in range(3):
        print(f"\n{i+1}. Pergunta: {perguntas[i]}")
        print(f"   Resposta: {respostas[i]}")

if __name__ == "__main__":
    main()
