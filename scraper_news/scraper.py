from typing import List
import requests
import logging

from .constants import REQUEST_HEADER, REQUEST_COOKIES
from .sources import get_source_info
from .filemanager import Filemanager
from .news import News


class ScraperNews:
    def __init__(self, source: str, is_breaking: bool = False) -> None:
        self.source: str = source.lower()
        self.is_breaking: bool = is_breaking
        self.news: List[News] = []
        self.logger = logging.getLogger(__name__)

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

        if response == None:
            return

        self.news = source_function(response, self.is_breaking)

    def print_news(self):
        """Print the news from the source"""
        print(f"{self.source.upper()}:")

        if len(self.news) == 0:
            no_news_string = "> No breaking news" if self.is_breaking else "> No news"
            print(no_news_string, "\n")
            return

        breaking_string = "BREAKING - " if self.is_breaking else ""
        for news in self.news:
            print(f"> {breaking_string}{news.title} - {news.url}")
        print()

    def save_news(self):
        """Save the news to the json file"""
        if len(self.news) == 0:
            # no_news_to_save_string = "No breaking news to save" if self.is_breaking else "No news to save"
            # print(f"{self.source.upper()} - {no_news_to_save_string}")
            return

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
    try:
        response = requests.get(url, headers=REQUEST_HEADER, cookies=REQUEST_COOKIES, timeout=60)
        # return BeautifulSoup(response.text, "html.parser")
        return response
    except requests.exceptions.RequestException:
        logging.getLogger(__name__).exception(f"Module requests exception with url: {url}")
        print("Requests error happen - check logfile")
        return None

def is_news_id_saved(news_id: str, saved_news: List[dict]) -> bool:
    for news in saved_news:
        if news["id"] == news_id:
            return True
    return False
