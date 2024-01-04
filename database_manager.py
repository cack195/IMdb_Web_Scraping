import sqlite3


def create_tables(connection):
    genres = [
        "Drama", "Comedy", "Sci-Fi", "Sport", "Film-Noir", "Adventure",
        "Mystery", "Biography", "Western", "Thriller", "War", "Family",
        "Horror", "Action", "Fantasy", "Animation", "Music", "Musical",
        "Crime", "Romance", "History"
    ]

    for genre in genres:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {genre.replace("-", "_")} (
                Movie_Number INTEGER PRIMARY KEY,
                Movie_Title TEXT,
                Movie_Link TEXT,
                Review_Title TEXT,
                Review_Content TEXT,
                Review_Link TEXT,
                CONSTRAINT unique_movie_review UNIQUE (Movie_Title, Review_Title)
            )
        ''')
        connection.commit()


def insert_movie_data(connection, genre, movie_data):
    table_name = genre.replace("-", "_")
    cursor = connection.cursor()

    for movie in movie_data:
        try:
            cursor.execute(f'''
                INSERT INTO {table_name} (Movie_Title, Movie_Link, Review_Title, Review_Content, Review_Link)
                VALUES (:Movie_Title, :Movie_Link, :Review_Title, :Review_Content, :Review_Link)
            ''', {
                "Movie_Title": movie["Movie Title"],
                "Movie_Link": movie["Movie Link"],
                "Review_Title": movie["Review"],
                "Review_Content": movie["Review content"],
                "Review_Link": movie["Review Link"]
            })
            connection.commit()
        except sqlite3.IntegrityError as e:
            # Handle duplicates
            print(f"Skipping duplicate: {movie['Movie Title']}, {movie['Review']}")
            connection.rollback()  # Rollback to prevent incomplete transactions

        except sqlite3.Error as e:
            # Handle other SQLite errors
            print(f"SQLite error: {e}")
            connection.rollback()  # Rollback to prevent incomplete transactions
        except Exception as e:
            # Handle other exceptions
            print(f"Error: {e}")
            connection.rollback()  # Rollback to prevent incomplete transactions


def connect_to_database(db_name='movies.db'):
    return sqlite3.connect(db_name)
