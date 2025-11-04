# setup_qa_db.py

import sqlite3

DB_NAME = 'qa.db'

# ----------------- CREATE TABLE -----------------
def create_table():
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
    print("✅ Table chatbot_data is ready in qa.db")

# ----------------- SAMPLE Q&A DATA -----------------
qa_data = [
    # ------------- Physics -------------
    ("What is Newton's first law of motion?", "An object remains at rest or moves with uniform velocity unless acted upon by an external force."),
    ("What is Ohm's Law?", "V = IR, where V is voltage, I is current, and R is resistance."),
    ("What is the SI unit of force?", "The SI unit of force is newton (N)."),
    ("Define acceleration.", "Acceleration is the rate of change of velocity per unit time."),
    ("State the law of conservation of energy.", "Energy can neither be created nor destroyed; it can only change from one form to another."),
    ("What is gravitational potential energy?", "Energy possessed by a body due to its position in a gravitational field."),
    ("What is the speed of light?", "The speed of light in vacuum is approximately 3 × 10^8 m/s."),
    ("What is a vector quantity?", "A physical quantity that has both magnitude and direction."),
    ("What is momentum?", "Momentum is the product of mass and velocity of a body."),
    ("Define impulse.", "Impulse is the change in momentum of a body when a force acts on it over time."),

    # ------------- Chemistry -------------
    ("What is Avogadro's number?", "6.022 × 10^23 particles per mole."),
    ("Define molarity.", "Molarity is the number of moles of solute per liter of solution."),
    ("What is the pH of pure water?", "pH of pure water is 7 at 25°C."),
    ("What is an acid according to Arrhenius?", "A substance that increases H⁺ concentration in aqueous solution."),
    ("What is the chemical formula of ammonia?", "NH₃."),
    ("State Le Chatelier's principle.", "If a system at equilibrium is disturbed, it shifts to counteract the disturbance."),
    ("Define oxidation.", "Loss of electrons by a substance."),
    ("Define reduction.", "Gain of electrons by a substance."),
    ("What is the atomic number of carbon?", "6."),
    ("What is the molecular mass of water?", "18 g/mol."),

    # ------------- Biology -------------
    ("What is photosynthesis?", "Process by which green plants make food using sunlight, water, and CO₂."),
    ("What is transpiration?", "Loss of water vapor from plants through stomata."),
    ("What is the functional unit of the kidney?", "The nephron."),
    ("What is the powerhouse of the cell?", "Mitochondria."),
    ("What is DNA?", "DNA is the genetic material that carries instructions for life."),
    ("Define osmosis.", "Movement of water molecules from low to high solute concentration through a semipermeable membrane."),
    ("What are enzymes?", "Biological catalysts that speed up chemical reactions."),
    ("What is the role of chlorophyll?", "It captures light energy for photosynthesis."),
    ("Define immunity.", "Ability of an organism to resist infection or disease."),
    ("What is a gene?", "A segment of DNA that codes for a specific trait."),

    # ------------- Additional Physics -------------
    ("What is kinetic energy?", "Energy possessed by a body due to its motion."),
    ("What is potential energy?", "Energy possessed by a body due to its position or configuration."),
    ("State Hooke's Law.", "Force applied on a spring is directly proportional to its extension within elastic limit."),
    ("Define work.", "Work is done when a force displaces a body in the direction of force."),
    ("Define power.", "Power is the rate at which work is done."),
    ("What is gravitational force?", "Attractive force between two masses proportional to the product of their masses and inversely proportional to the square of the distance."),

    # ------------- Additional Chemistry -------------
    ("What is ionic bond?", "Electrostatic attraction between oppositely charged ions."),
    ("What is covalent bond?", "Sharing of electron pairs between atoms."),
    ("Define electronegativity.", "Ability of an atom to attract shared electrons in a bond."),
    ("What is a catalyst?", "Substance that increases the rate of reaction without being consumed."),

    # ------------- Additional Biology -------------
    ("What is the function of ribosomes?", "Synthesize proteins in the cell."),
    ("What is mitosis?", "Cell division producing two identical daughter cells."),
    ("What is meiosis?", "Cell division producing four genetically different gametes."),
    ("What is osmoregulation?", "Regulation of water and salt balance in organisms."),
    ("What is blood plasma?", "The liquid component of blood that carries cells and nutrients."),
]

# ----------------- INSERT Q&A -----------------
def insert_qa():
    create_table()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for q, a in qa_data:
        cursor.execute("SELECT id FROM chatbot_data WHERE question=?", (q,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO chatbot_data (question, answer) VALUES (?, ?)", (q, a))

    conn.commit()
    conn.close()
    print("✅ qa.db created and populated with 12th standard Q&A.")

# ----------------- RUN -----------------
if __name__ == "__main__":
    insert_qa()
