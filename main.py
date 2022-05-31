from scraper_news import ScraperNews, request_url, argparse_setup
from bs4 import BeautifulSoup


def main():
    args = argparse_setup()

    for source in args.sources:
        s = ScraperNews(source, args.breaking)
        s.get_news()
        s.save_news()


if __name__ == "__main__":
    main()
