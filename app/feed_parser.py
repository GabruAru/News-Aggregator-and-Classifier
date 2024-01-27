import feedparser
import logging

def parse_rss_feeds(rss_feeds):
    articles = []
    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            article = {
                'title': entry.title,
                'content': getattr(entry, 'summary', ''),
                'publication_date': getattr(entry, 'published', ''),
                'source_url': entry.link
            }
            articles.append(article)
    logging.info(f'Parsed {len(articles)} articles from RSS feeds')       
    return articles
