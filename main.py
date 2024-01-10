from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from database_manager import connect_to_database, create_tables, insert_movie_data


def find_movies_and_store():
    genres = [
        "Drama", "Comedy", "Sci-Fi", "Sport", "Film-Noir", "Adventure",
        "Mystery", "Biography", "Western", "Thriller", "War", "Family",
        "Horror", "Action", "Fantasy", "Animation", "Music", "Musical",
        "Crime", "Romance", "History"
    ]

    connection = connect_to_database()
    create_tables(connection)

    for genre in genres:
        root = 'https://www.imdb.com/'
        my_url = f"{root}chart/top/?genres={genre}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        req = Request(my_url, headers=headers)
        uClient = urlopen(req)
        page_html = uClient.read()
        uClient.close()

        print(f'\n\n{genre} genre\n\n')
        html_text = BeautifulSoup(page_html, "lxml")

        movie_data = []
        while True:
            movies_list = html_text.find_all('li', class_='ipc-metadata-list-summary-item')
            for index, movies in enumerate(movies_list[:20], 1):
                movie_link = movies.find('a', class_='ipc-title-link-wrapper').attrs['href']
                movie_link = movie_link.rsplit('/', 1)[0]
                movie_title = movies.find('h3', class_='ipc-title__text').text

                movie_reviews_url = f"{root}{movie_link}/reviews?sort=submissionDate&dir=desc&ratingFilter=0"
                req_reviews = Request(movie_reviews_url, headers=headers)
                uClient_reviews = urlopen(req_reviews)
                page_html_reviews = uClient_reviews.read()
                uClient_reviews.close()

                html_text_reviews = BeautifulSoup(page_html_reviews, "lxml")
                reviews = html_text_reviews.find('div', class_='review-container')

                review_url = reviews.find('a', class_='title').attrs['href']
                movie_review_title = reviews.find('a', class_='title').text.strip()
                movie_review_url = f"{review_url}"
                review_content = html_text_reviews.find('div', class_='text show-more__control').text
                print(f'Collecting Movie {index}')
                movie_data.append({
                    "Movie Number": index,
                    "Movie Title": movie_title,
                    "Movie Link": f"{root}{movie_link}",
                    "Review": f"{movie_review_title}",
                    "Review content": f"{review_content}",
                    "Review Link": f"{root}{movie_review_url}"
                })
            insert_movie_data(connection, genre, movie_data)
    connection.close()


find_movies_and_store()
