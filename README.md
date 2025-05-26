# Articles Code Challenge

A Python project implementing an object-relational model for managing authors, magazines, and articles, with a SQLite database and a command-line interface (CLI).

## Project Structure
- `lib/db/`: Database connection, schema, and seed scripts.
- `lib/models/`: Model classes (`Author`, `Article`, `Magazine`).
- `tests/`: Pytest unit tests.
- `scripts/`: Setup and CLI scripts.

## Setup
1. Ensure Python 3.8+ is installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
