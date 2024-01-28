from celery import Celery
from .feed_parser import parse_rss_feeds
from .create_database import create_database
from .database import saving_articles
from .classifier import classify_article
from .html_parser import handle_content

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task(rate_limit='50/m')
def process_articles(rss_feeds):
    
    articles = parse_rss_feeds(rss_feeds)
    handle_content(articles)
    for article in articles:
        category = classify_article(article)
        article['category'] = category
    create_database()   
    saving_articles(articles)    


