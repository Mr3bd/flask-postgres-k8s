from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )

@app.route("/books", methods=["GET"])
def get_books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM books;")
    books = [{"id": row[0], "title": row[1]} for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    title = data.get("title")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title) VALUES (%s) RETURNING id;", (title,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": new_id, "title": title}), 201

@app.route("/health", methods=["GET"])
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

