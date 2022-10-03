
from datetime import datetime, timedelta
from typing import Dict, List
from scraper_news.filemanager import Filemanager

from scraper_news.news import News


def get_news_from_sources(sources: List[str]) -> Dict[str, List[News]]:
    news_json = Filemanager.get_news_data()

    for source_name in sources:
        if not news_json.get(source_name):
            print(f"\n{source_name.upper()} is not a supported source")
            sources.remove(source_name)

    # add sources as keys to dict with empty list as value
    news_from_sources = {source: [] for source in sources}

    for source_name, news_list in news_json.items():
        if source_name not in sources:
            continue

        for news_info in news_list:
            title = news_info["title"]
            url = news_info["url"]
            is_breaking = news_info["is_breaking"]
            time_saved = news_info["time_saved"]
            news = News(title, url, source_name, is_breaking=is_breaking, time_saved=time_saved)
            news_from_sources[source_name].append(news)

    return news_from_sources


def get_news_in_time_frame_back(hours_from: int, hours_to: int, news_list: List[News], must_be_breaking: bool) -> List[News]:
    time_now = datetime.now()
    time_hours_from = time_now - timedelta(hours=hours_from)
    time_hours_to = time_now - timedelta(hours=hours_to)

    news_in_time_frame = []

    for news in news_list:
        if must_be_breaking and not news.is_breaking:
            continue

        news_time = datetime.strptime(news.time_saved, "%Y-%m-%d - %H:%M:%S")
        if not time_hours_to > news_time or not news_time > time_hours_from:
            continue

        news_in_time_frame.append(news)

    return news_in_time_frame
