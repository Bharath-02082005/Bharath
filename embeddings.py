# embeddings.py
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer

DB_NAME = 'qa.db'
MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

# Load model
model = SentenceTransformer(MODEL_NAME)

# Fetch all questions and answers from DB
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute("SELECT question, answer FROM chatbot_data")
data = cursor.fetchall()
conn.close()

# Split questions and answers
questions = [q for q, a in data]
answers = [a for q, a in data]

# Compute embeddings
question_embeddings = model.encode(questions, convert_to_tensor=True)

print("✅ Embeddings computed for all Q&A")
