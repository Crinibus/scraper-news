from typing import List
import logging.config
from scraper_news import ScraperNews, argparse_setup, Filemanager
import scraper_news


def main():
    args = argparse_setup()

    if args.count:
        count_news()

    if args.scrape:
        scrape_news(args.sources, args.breaking)

    if args.show:
        scraper_news.show_news_in_time_frame(args.sources, args.hours, args.breaking)


def scrape_news(sources: List[str], is_breaking: bool):
    for source in sources:
        s = ScraperNews(source, is_breaking)
        s.get_news()
        s.print_news()
        s.save_news()


def count_news() -> None:
    news = Filemanager.get_news_data()

    for source_name, news_list in news.items():
        print(f"\n{source_name.upper()}")
        print(f"Number of news: {len(news_list)}")
    print()


if __name__ == "__main__":
    logging.config.fileConfig(
        fname=Filemanager.logging_ini_path,
        defaults={"logfilename": Filemanager.logfile_path},
    )

    main()
