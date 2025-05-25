import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DROP TABLE IF EXISTS articles;
        DROP TABLE IF EXISTS authors;
        DROP TABLE IF EXISTS magazines;
    """)
    with open('lib/db/schema.sql', 'r') as f:
        cursor.executescript(f.read())
    cursor.executescript("""
        INSERT INTO authors (name) VALUES ('Test Author');
        INSERT INTO magazines (name, category) VALUES ('Test Mag', 'Tech');
        INSERT INTO articles (title, author_id, magazine_id) VALUES ('Test Article', 1, 1);
    """)
    conn.commit()
    conn.close()

def test_author_creation(setup_db):
    author = Author("Jane Doe")
    assert author.name == "Jane Doe"
    assert author.id is not None

def test_author_articles(setup_db):
    author = Author.find_by_id(1)
    articles = author.articles()
    assert len(articles) == 1
    assert articles[0]['title'] == "Test Article"
