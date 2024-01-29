from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging 
import os
import csv

load_dotenv()
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    publication_date = Column(String)
    source_url = Column(String)
    category = Column(String)

username = os.environ['user']
password = os.environ['password']
database_name = os.environ['Database_Name']


def get_session():
    engine = create_engine(f'postgresql://{username}:{password}@localhost/{database_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    
    return Session()

def save_articles(articles, session):
    for article_data in articles:
        existing_article = session.query(Article).filter_by(title=article_data['title'], source_url=article_data['source_url']).first()
        if existing_article:
            logging.info(f"Article '{article_data['title']}' already exists in the database. Skipping...")
            continue
        article = Article(**article_data)
        session.add(article)
    session.commit()
    logging.info("Articles saved successfully")
    

def saving_articles(articles):
    session = get_session()
    save_articles(articles, session)

def export_to_csv(filename):
    session = get_session()
    articles = session.query(Article).all()
    print(articles)
    csv_columns = ['id', 'title', 'content', 'publication_date', 'source_url', 'category']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for article in articles:
            writer.writerow({'id': article.id,
                             'title': article.title,
                             'content': article.content,
                             'publication_date': article.publication_date,
                             'source_url': article.source_url,
                             'category': article.category})
    logging.info(f"Exported articles to {filename}")    