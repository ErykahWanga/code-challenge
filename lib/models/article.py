from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine

class Article:
    """Represents an article with a title, author, and magazine."""
    def __init__(self, title, author, magazine, id=None):
        """Initialize an article with title, author, magazine, and optional ID.

        Args:
            title (str): The title of the article.
            author (Author): The author instance.
            magazine (Magazine): The magazine instance.
            id (int, optional): The article's ID. Defaults to None.
        Raises:
            ValueError: If title is not a non-empty string or author/magazine are invalid.
        """
        self._id = id
        self._title = None
        self._author = None
        self._magazine = None
        self.title = title
        self.author = author
        self.magazine = magazine
        if id is None:
            self.save()

    @property
    def id(self):
        """Get the article's ID.

        Returns:
            int: The article's ID.
        """
        return self._id

    @property
    def title(self):
        """Get the article title.

        Returns:
            str: The article title.
        """
        return self._title

    @title.setter
    def title(self, value):
        """Set the article title.

        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        """Get the article's author.

        Returns:
            Author: The author instance.
        """
        return self._author

    @author.setter
    def author(self, value):
        """Set the article's author.

        Args:
            value (Author): The author instance.

        Raises:
            ValueError: If value is not an Author instance.
        """
        if not isinstance(value, Author):
            raise ValueError("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        """Get the article's magazine.

        Returns:
            Magazine: The magazine instance.
        """
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        """Set the article's magazine.

        Args:
            value (Magazine): The magazine instance.

        Raises:
            ValueError: If value is not a Magazine instance.
        """
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = value

    def save(self):
        """Save the article to the database and set its ID."""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (self.title, self.author.id, self.magazine.id)
            )
            self._id = cursor.lastrowid
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an article by its ID.

        Args:
            id (int): The article's ID.

        Returns:
            Article: The article instance, or None if not found.
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            author = Author.find_by_id(row['author_id'])
            magazine = Magazine.find_by_id(row['magazine_id'])
            return cls(row['title'], author, magazine, row['id'])
        return None
