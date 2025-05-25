from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    while True:
        print("\n1. List all authors")
        print("2. List all magazines")
        print("3. List articles by author")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            for row in cursor.fetchall():
                print(dict(row))
            conn.close()
        elif choice == "2":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines")
            for row in cursor.fetchall():
                print(dict(row))
            conn.close()
        elif choice == "3":
            author_id = input("Enter author ID: ")
            author = Author.find_by_id(int(author_id))
            if author:
                print(author.articles())
            else:
                print("Author not found")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()