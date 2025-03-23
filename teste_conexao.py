import psycopg2

try:
    conn = psycopg2.connect(
        dbname="chatbot",
        user="postgres",
        password="Lila369*",
        host="localhost",
        port="5432"
    )
    print("✅ Conexão bem-sucedida com o PostgreSQL!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar com o PostgreSQL:")
    print(e)
