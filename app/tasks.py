from celery import Celery
from .feed_parser import parse_rss_feeds
from .create_database import create_database
from .database import saving_articles
from .database import export_to_csv
from .html_parser import handle_content
from .classifier import classify_article
from celery.result import AsyncResult
import logging

def process_articles(rss_feeds):
    articles = parse_rss_feeds(rss_feeds)
    handle_content(articles)
    logging.info(f"Articles Classification with celery in progress..")    
    article_task_mapping = {}

    for article in articles:
        category_task = classify_article.delay(article)
       
        article_task_mapping[category_task.id] = article


    for task_id, article in article_task_mapping.items():
     
        result = classify_article.AsyncResult(task_id)
        category = result.get()
        
        article['category'] = category
        
    logging.info(f"Articles Classification with celery Completed..")        
    
    create_database()
    saving_articles(articles)
    export_to_csv('articles.csv')
