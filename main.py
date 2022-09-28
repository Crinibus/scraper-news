import threading
from typing import List
import logging.config
from scraper_news import ScraperNews, request_url, argparse_setup, Filemanager
from bs4 import BeautifulSoup


def main():
    args = argparse_setup()

    if args.scrape:
        if args.threads:
            scrape_news_threads(args.sources, args.breaking)
        else:
            scrape_news(args.sources, args.breaking)


def scrape_news(sources: List[str], is_breaking: bool):
    for source in sources:
        s = ScraperNews(source, is_breaking)
        s.get_news()
        s.print_news()
        s.save_news()


def scrape_news_threads(sources: List[str], is_breaking: bool):
    news_sources = [ScraperNews(source, is_breaking) for source in sources]

    threads = [threading.Thread(target=news_source.get_news) for news_source in news_sources]

    # Start scraping on all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print and save news (sequentially)
    for news_source in news_sources:
        news_source.print_news()
        news_source.save_news()


if __name__ == "__main__":
    logging.config.fileConfig(
        fname=Filemanager.logging_ini_path,
        defaults={"logfilename": Filemanager.logfile_path},
    )

    main()
