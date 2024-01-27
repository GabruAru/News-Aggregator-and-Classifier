import logging
import os
from app.tasks import process_articles
from app.feed_parser import parse_rss_feeds

logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    rss_directory = 'feeds_data/'

    # Get a list of all files in the directory
    rss_files = [os.path.join(rss_directory, f) for f in os.listdir(rss_directory) if os.path.isfile(os.path.join(rss_directory, f))]
    
    process_articles(rss_files)

