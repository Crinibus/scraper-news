from typing import List

from scraper_news.get_news import get_news_from_sources, get_news_in_time_frame_back


def show_news_in_time_frame(sources: List[str], hours_from_to: str, must_be_breaking: bool) -> None:
    news_dict = get_news_from_sources(sources)

    hours_list = hours_from_to.split("-")
    hours_from = int(hours_list[0])
    hours_to = int(hours_list[1]) if len(hours_list) > 1 else 0

    if (hours_to > hours_from):
        hours_from, hours_to = hours_to, hours_from

    for source_name, news_list in news_dict.items():
        print(f"\n{source_name.upper()}")

        news_in_time_frame = get_news_in_time_frame_back(hours_from, hours_to, news_list, must_be_breaking)

        if not news_in_time_frame:
            if must_be_breaking:
                no_news_message = f"No breaking news in the between {hours_from}-{hours_to} hours back"
            else:
                no_news_message = f"No news in the between {hours_from}-{hours_to} hours back"
            print(no_news_message)
            continue

        for news in news_in_time_frame:
            news_title = f"BREAKING - {news.title}" if news.is_breaking else news.title
            print(f"> {news_title}")
            print(f"  - {news.time_saved}")
            print(f"  - {news.url}\n")
