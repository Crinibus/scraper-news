from typing import List
from scraper_news import ScraperNews, request_url, argparse_setup
from bs4 import BeautifulSoup


def main():
    args = argparse_setup()

    if args.scrape:
        scrape_news(args.sources, args.breaking)


def scrape_news(sources: List[str], is_breaking: bool):
    for source in sources:
        s = ScraperNews(source, is_breaking)
        s.get_news()
        s.print_news()
        s.save_news()


if __name__ == "__main__":
    main()
