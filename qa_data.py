# qa_data.py

import sqlite3
import os

DB_NAME = 'qa.db'  # Database file name

# ----------------- DATABASE FUNCTIONS -----------------
def create_table():
    """Create chatbot_data table if it doesn't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chatbot_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(question, answer):
    """Save chatbot Q&A to database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chatbot_data (question, answer) VALUES (?, ?)",
        (question, answer)
    )
    conn.commit()
    conn.close()

def get_all_data():
    """Retrieve all Q&A from database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chatbot_data")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ----------------- INITIAL Q&A DATA -----------------
initial_data = [
    # ----------- Physics -----------
    ("What is Newton's first law of motion?", "An object will remain at rest or in uniform motion unless acted upon by an external force."),
    ("What is Ohm's Law?", "Ohm's Law states that V = IR, where V is voltage, I is current, and R is resistance."),
    ("What is the speed of light?", "The speed of light in vacuum is approximately 3 × 10^8 m/s."),
    ("What is a vector quantity?", "A physical quantity that has both magnitude and direction, such as velocity or force."),
    ("What is the SI unit of force?", "The SI unit of force is the newton (N)."),

    # ----------- Chemistry -----------
    ("What is the atomic number of carbon?", "The atomic number of carbon is 6."),
    ("What is the pH of pure water?", "The pH of pure water is 7 at 25°C."),
    ("What is Avogadro's number?", "Avogadro's number is 6.022 × 10^23 particles per mole."),
    ("What is an acid according to Arrhenius?", "An acid is a substance that increases the concentration of hydrogen ions (H⁺) in solution."),
    ("What is the chemical formula of ammonia?", "The chemical formula of ammonia is NH₃."),

    # ----------- Biology -----------
    ("What is the functional unit of the kidney?", "The functional unit of the kidney is the nephron."),
    ("What is photosynthesis?", "Photosynthesis is the process by which green plants make food using sunlight, carbon dioxide, and water."),
    ("What is the genetic material in most living organisms?", "DNA is the genetic material in most living organisms."),
    ("What is the powerhouse of the cell?", "The mitochondrion is known as the powerhouse of the cell."),
    ("What is transpiration?", "Transpiration is the process by which water is lost from plants as water vapor through stomata."),
]

# ----------------- INSERT INITIAL DATA -----------------
def insert_initial_data():
    create_table()  # Ensure table exists first
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Insert only if question does not already exist
    for question, answer in initial_data:
        cursor.execute(
            "SELECT id FROM chatbot_data WHERE question = ?",
            (question,)
        )
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO chatbot_data (question, answer) VALUES (?, ?)",
                (question, answer)
            )
    conn.commit()
    conn.close()
    print("✅ Initial Q&A data inserted successfully!")

# ----------------- RUN ONLY WHEN SCRIPT IS EXECUTED -----------------
if __name__ == "__main__":
    insert_initial_data()
    # Optional: print all data to verify
    for row in get_all_data():
        print(row)
