# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3
from sentence_transformers import SentenceTransformer, util
import torch
import os

app = Flask(__name__)
DB_NAME = 'qa.db'

# Load AI model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# ----------------- Helper functions -----------------
def save_to_history(sender, message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Ensure timestamp is saved automatically
    cursor.execute("INSERT INTO chat_history (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT sender, message, timestamp FROM chat_history ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    # Return list of dicts with sender, message, timestamp
    return [{"sender": sender, "message": msg, "timestamp": timestamp} for sender, msg, timestamp in rows]

# ----------------- Routes -----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form.get("msg")
    if not user_msg:
        return "Please type something!"

    save_to_history("You", user_msg)

    # Search in database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM chatbot_data")
    rows = cursor.fetchall()
    conn.close()

    questions = [q for q, _ in rows]
    answers = [a for _, a in rows]

    if questions:
        question_embeddings = model.encode(questions, convert_to_tensor=True)
        user_embedding = model.encode(user_msg, convert_to_tensor=True)
        similarities = util.cos_sim(user_embedding, question_embeddings)[0]
        best_idx = torch.argmax(similarities).item()

        if similarities[best_idx] > 0.5:
            bot_reply = answers[best_idx]
        else:
            bot_reply = "Sorry, I don't know the answer. Try a different question."
    else:
        bot_reply = "Database is empty."

    save_to_history("Bot", bot_reply)
    return bot_reply

@app.route("/image", methods=["POST"])
def image_upload():
    if 'image' not in request.files:
        return "No image uploaded!"
    image_file = request.files['image']
    filename = image_file.filename
    save_path = os.path.join("static", "uploads")
    os.makedirs(save_path, exist_ok=True)
    filepath = os.path.join(save_path, filename)
    image_file.save(filepath)

    reply = f"Image '{filename}' uploaded successfully! (Processing not implemented)"

    save_to_history("You", f"[Image] {filename}")
    save_to_history("Image Bot", reply)
    return reply

@app.route("/history")
def history():
    return jsonify(get_history())  # Now includes timestamps

# ----------------- Run -----------------
if __name__ == "__main__":
    app.run(debug=True)
