# IMDb Movie Scraper and Database Manager

This project scrapes IMDb's top movies for various genres, fetches their reviews, and stores the data in a SQLite database.

## Features

- **Movie Data Scraping:** Utilizes BeautifulSoup to extract movie information and reviews from IMDb.
- **Database Management:** Stores scraped data in a SQLite database with genre-specific tables.
- **Error Handling:** Handles duplicates and potential errors during data insertion.

## Setup Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/IMdb_Web_Scraping.git
    cd IMdb_Web_Scraping
    ```

2. **Environment Setup**

    - Ensure you have Python installed (preferably Python 3.x).
    - Install required dependencies:

        ```bash
        pip install -r requirements.txt
        ```

3. **Database Configuration**

    - The default database name is `movies.db`. Change the name in `database_manager.py` if required.

4. **Run the Scraper**

    ```bash
    python main.py
    ```

## Project Structure

- **`main.py`:** Contains the main logic for scraping IMDb and storing data.
- **`database_manager.py`:** Manages SQLite database creation and data insertion.
- **`requirements.txt`:** Lists project dependencies.

## Viewing Database Diagram

- For viewing the database diagram, open the `draw.io` tool and import the `Database_Diagram` file located in the project root directory.

