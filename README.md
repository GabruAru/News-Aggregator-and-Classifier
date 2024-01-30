# News-Aggregator-and-Classifier
News Article Classifier is a Python application that collects news articles from various RSS feeds, stores them in a PostgreSQL database, and categorizes them into predefined categories using natural language processing techniques with LLM. The application is built using Python, Celery for task queue management, SQLAlchemy for database interaction, and Langchain.


## Features
- Collects news articles from various RSS feeds.
- Stores articles in a PostgreSQL database with duplicate handling.
- Categorizes articles into predefined categories such as Terrorism/Protest/Political Unrest/Riot, Positive/Uplifting, Natural Disasters, and Others.
- Asynchronously processes articles using Celery for efficient task management.
- Provides error handling and logging mechanisms for robustness.
- Supports exporting articles to CSV format for easy analysis.

## Requirements
- Python 
- PostgreSQL
- Redis

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/news-article-classifier.git
    ```
2. Create virtual Environment:
     ```bash
    python -m venv venv 
    ```
   
3. Install dependencies:

    ```bash
    cd news-article-classifier
    pip install -r requirements.txt
    ```

4. Set up PostgreSQL and Redis servers.

  - For windows. First install Docker and run redis server with this
    ```bash
    docker run -d -p 6379:6379 --name redis-con redis:latest
    ```
    
5. Configure environment variables:
    - Create a `.env` file in the project root.
    - Add the following environment variables:
        - `LLama_API`: Your LLama API key.
        - `Database_Name`: Name of your PostgreSQL database.
        - `user`: PostgreSQL username.
        - `password`: PostgreSQL password.
     
6. Intialize the celery worker:

    ```bash
    celery -A app.worker worker --loglevel=info -P eventlet
     ```
    
7. Run the application:

    ```bash
    python main.py
    ```
    
## Usage

1. Add RSS feed URLs to the `main.py` file.
2. Run `main.py` to start processing articles.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of  Celery, SQLAlchemy, and other libraries used in this project.
- Special thanks to LLama for providing the API used for text classification.
    
 
    
