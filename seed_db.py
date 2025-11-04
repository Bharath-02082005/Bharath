# seed_db.py
import sqlite3

# Connect to your existing database file (qa.db)
# (if it doesn't exist, it will be created automatically)
conn = sqlite3.connect('qa.db')
cursor = conn.cursor()

# Create a table for storing chatbot Q&A
cursor.execute('''
CREATE TABLE IF NOT EXISTS chatbot_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Optional: Seed some initial Q&A into the chatbot
initial_data = [
    ("What is AI?", "AI stands for Artificial Intelligence, which enables machines to perform tasks that normally require human intelligence."),
    ("What is Deep Learning?", "Deep Learning is a subset of AI that uses neural networks with many layers to learn from data."),
    ("How can this chatbot help me?", "It can answer your syllabus-related questions and provide study guidance."),
    ("Who developed this chatbot?", "This chatbot is developed as a project for 12th standard students.")
]

# Insert initial data into the table if it's empty
cursor.execute("SELECT COUNT(*) FROM chatbot_data")
count = cursor.fetchone()[0]
if count == 0:
    cursor.executemany("INSERT INTO chatbot_data (question, answer) VALUES (?, ?)", initial_data)
    print(f"✅ Inserted {len(initial_data)} initial Q&A entries.")
else:
    print("ℹ️ Chatbot data already exists in the database.")

conn.commit()
conn.close()
print("✅ Database setup completed successfully!")
