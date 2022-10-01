from typing import List

from scraper_news.get_news import get_news_from_sources, get_news_in_time_frame_back


def show_news_in_time_frame(sources: List[str], hours: int, must_be_breaking: bool) -> None:
    news_dict = get_news_from_sources(sources)

    for source_name, news_list in news_dict.items():
        print(f"\n{source_name.upper()}")

        news_in_time_frame = get_news_in_time_frame_back(hours, news_list, must_be_breaking)

        if not news_in_time_frame:
            if must_be_breaking:
                no_news_message = f"No breaking news in the last {hours} hours"
            else:
                no_news_message = f"No news in the last {hours} hours"
            print(no_news_message)
            continue

        for news in news_in_time_frame:
            news_title = f"BREAKING - {news.title}" if news.is_breaking else news.title
            print(f"> {news_title}")
            print(f"  - {news.time_saved}")
            print(f"  - {news.url}\n")
