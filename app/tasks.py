from celery import Celery
from .feed_parser import parse_rss_feeds
from .create_database import create_database
from .database import saving_articles
from .classifier import classify_article

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_articles(rss_feeds):
    
    articles = parse_rss_feeds(rss_feeds)
    for article in articles:
        category = classify_article(article)
        article['category'] = category
    create_database()   
    saving_articles(articles)    


