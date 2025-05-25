import os
from lib.db.connection import get_connection
from lib.db.seed import seed_database

def setup_database():
    db_file = 'articles.db'
    if os.path.exists(db_file):
        os.remove(db_file)
    
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    seed_database()

if __name__ == "__main__":
    setup_database()
