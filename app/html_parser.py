import html2text
import logging

h = html2text.HTML2Text()

h.ignore_links = True


def handle_content(articles):
    for article in articles:
        article['content'] = h.handle(article['content'])
    logging.info(f"Processed HTML format content for {len(articles)} articles Successfully")    
    return articles    