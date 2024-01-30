import logging
import os
from app.tasks import process_articles

logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    # rss_directory = 'feeds_data/'

    # rss_files = [os.path.join(rss_directory, f) for f in os.listdir(rss_directory) if os.path.isfile(os.path.join(rss_directory, f))]

    rss_feeds = [
        "http://rss.cnn.com/rss/cnn_topstories.rss",
        "http://qz.com/feed",
        "http://feeds.foxnews.com/foxnews/politics",
        "http://feeds.reuters.com/reuters/businessNews",
        "http://feeds.feedburner.com/NewshourWorld",
        "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml",
    ]

    process_articles(rss_feeds)
