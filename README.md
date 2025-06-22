# Project 2: Pull Data from API and Store in SQLite

In this project, I pulled data from the PokéAPI, cleaned it using Python, and saved it to a local SQLite database.

---

## Files
- `project2_api_to_sqlite.py`: Python script that pulls, cleans, and stores the data
- `pokemon.db`: SQLite database containing the Pokémon table

---

## What I Did
- Fetched Pokémon data from a public API (`https://pokeapi.co/api/v2/pokemon/pikachu`)
- Extracted only the required fields (name, height, base experience)
- Cleaned and formatted the data
- Created a SQLite database and inserted the data into a table
- Queried the table to verify the data was saved correctly

---

## Tools Used
- Python
- Requests
- SQLite (via `sqlite3` module)

---

## What This Shows
This project demonstrates my ability to:
- Work with APIs
- Clean and structure raw JSON data
- Build a basic ETL process (Extract, Transform, Load)
- Use SQL within Python to store and retrieve data
