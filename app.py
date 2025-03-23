from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Carrega as variáveis do .env
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo
class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

# Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("⚠️ ERRO: A chave da API do Gemini não foi encontrada.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def responder_pergunta(pergunta):
    try:
        resposta = model.generate_content(pergunta)
        return resposta.text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

# 🔥 Rota principal para o chatbot
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")
    resposta_ia = responder_pergunta(user_message)
    return jsonify({"response": resposta_ia})

if __name__ == "__main__":
    from os import environ
    if environ.get("RENDER") != "true":
        app.run(debug=True, port=5000)
