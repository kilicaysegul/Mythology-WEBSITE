from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sqlite3
from pydantic import BaseModel

app = FastAPI()

# Statik dosyaları "sounds" klasöründen sunabilmesi için
app.mount("/sounds", StaticFiles(directory="sounds"), name="sounds")

# SQLite veritabanı bağlantısı
conn = sqlite3.connect('greek_mythology.db')
cursor = conn.cursor()

# SQLite veritabanında gerekli tabloları oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS gods (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
)''')

# Başlangıçta bazı tanrılar ekleyelim
cursor.execute('''INSERT INTO gods (name, description) VALUES
    ("Zeus", "Zeus is the king of the gods, associated with thunder and lightning."),
    ("Hera", "Hera is the queen of the gods and goddess of marriage."),
    ("Poseidon", "Poseidon is the god of the sea, earthquakes, and horses."),
    ("Athena", "Athena is the goddess of wisdom, war, and craft.")
''')

conn.commit()

# Pydantic model for the Gods
class God(BaseModel):
    name: str
    description: str

@app.get("/gods")
async def get_gods():
    cursor.execute("SELECT * FROM gods")
    gods = cursor.fetchall()
    return [{"id": god[0], "name": god[1], "description": god[2]} for god in gods]

@app.post("/gods")
async def create_god(god: God):
    cursor.execute("INSERT INTO gods (name, description) VALUES (?, ?)", (god.name, god.description))
    conn.commit()
    return {"name": god.name, "description": god.description}

@app.get("/gods/{god_id}")
async def get_god(god_id: int):
    cursor.execute("SELECT * FROM gods WHERE id = ?", (god_id,))
    god = cursor.fetchone()
    if god:
        return {"id": god[0], "name": god[1], "description": god[2]}
    return {"error": "God not found"}



