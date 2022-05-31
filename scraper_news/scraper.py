from typing import List
import requests

from .constants import REQUEST_HEADER, REQUEST_COOKIES
from .sources import get_source_info
from .filemanager import Filemanager
from .news import News


class ScraperNews:
    def __init__(self, source: str, is_breaking: bool = False) -> None:
        self.source: str = source.lower()
        self.is_breaking: bool = is_breaking
        self.news: List[News] = []

    def get_news(self) -> None:
        """Scrape news from the source"""
        source_info = get_source_info(self.source)

        if not source_info:
            print(f"Source is not supported: {self.source}")
            return None

        news_category = "breaking" if self.is_breaking else "news"
        link = source_info[news_category]
        source_function = source_info["function"]

        response = request_url(link)
        self.news = source_function(response, self.is_breaking)

    def print_news(self):
        """Print the news from the source"""
        print(f"{self.source.upper()}:")
        for news in self.news:
            breaking_string = "BREAKING - " if news.is_breaking else ""
            print(f"> {breaking_string}{news.title} - {news.url}")

    def save_news(self):
        """Save the news to the json file"""
        news_data = Filemanager.get_news_data()

        if not news_data.get(self.source):
            news_data[self.source] = []

        source_news = news_data[self.source]

        for news in self.news:
            if is_news_id_saved(news.id, source_news):
                continue

            source_news.append(news.get_json())

        Filemanager.save_news_data(news_data)


def request_url(url: str) -> requests.models.Response:
    response = requests.get(url, headers=REQUEST_HEADER, cookies=REQUEST_COOKIES, timeout=60)
    # return BeautifulSoup(response.text, "html.parser")
    return response


def is_news_id_saved(news_id: str, saved_news: List[dict]) -> bool:
    for news in saved_news:
        if news["id"] == news_id:
            return True
    return False
