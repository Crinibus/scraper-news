from typing import List
from bs4 import BeautifulSoup
import requests
import json

from .news import News


def get_source_info(source: str) -> dict:
    return sources_info.get(source, None)


def dr(response: requests.models.Response, is_breaking: bool) -> str:
    return response.text


def tv2(response: requests.models.Response, is_breaking: bool) -> List[News]:
    json_news = response.json()

    news_info = []
    for news in json_news:
        title = news["title"]
        url = news["url"]
        id = news["id"]
        seq = news["seq"]
        news_info.append(News(title, url, id, seq, is_breaking))

    return news_info


sources_info = {
    "tv2": {
        "news": "",
        "breaking": "https://shared.tv2.dk/t2breakingbar",
        "function": tv2,
    },
    "dr": {
        "news": "https://www.dr.dk/nyheder/service/feeds/senestenyt",
        "breaking": "",
        "function": dr,
    },
}
