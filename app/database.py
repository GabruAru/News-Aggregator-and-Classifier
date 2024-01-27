from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging 
import os

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
engine = create_engine(f'postgresql://{username}:{password}@localhost/{database_name}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def save_articles(articles):
    for article_data in articles:
        article = Article(**article_data)
        session.add(article)
    session.commit()
    logging.info("Articles saved successfully")  # Add logging statement for information
