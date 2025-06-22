import requests
import sqlite3

# Example API call (hardcoded for simplicity)
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
data = response.json()

# Extract relevant fields
name = data["name"].title()
height = data["height"]
base_experience = data["base_experience"]

# Store in dictionary
pokemon = {
    "name": name,
    "height": height,
    "base_experience": base_experience
}

# Save to SQLite
conn = sqlite3.connect("pokemon.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    name TEXT,
    height INTEGER,
    base_experience INTEGER
)
""")

cursor.execute(
    "INSERT INTO pokemon (name, height, base_experience) VALUES (?, ?, ?)",
    (pokemon["name"], pokemon["height"], pokemon["base_experience"])
)

conn.commit()
conn.close()

print("Data saved successfully to pokemon.db")
