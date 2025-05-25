import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
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

def test_article_creation(setup_db):
    author = Author.find_by_id(1)
    assert author is not None, "Author with id=1 not found"
    magazine = Magazine.find_by_id(1)
    assert magazine is not None, "Magazine with id=1 not found"
    article = Article("New Article", author, magazine)
    assert article.title == "New Article"
    assert article.author.id == author.id
    assert article.magazine.id == magazine.id
