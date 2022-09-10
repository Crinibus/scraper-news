from typing import List
# from bs4 import BeautifulSoup
import re
import requests
from lxml import etree

from .news import News


def get_source_info(source: str) -> dict:
    return sources_info.get(source, None)


# def parse_dr_xml_text(xml_text):
#     return xml_text.strip().replace("<![CDATA[", "").replace("]]>", "")


def dr(response: requests.models.Response, is_breaking: bool) -> str:
    xml_parser = etree.XMLParser()
    xml_parser.feed(response.text)
    root = xml_parser.close()
    news_items = root[0][8:]

    news_info = []
    for news in news_items:
        id = news.find("guid").text
        title = news.find("title").text
        print("Title: ", title)
        url = news.find("link").text
        pubdate = news.find("pubDate").text
        news_info.append(News(title, url, id, seq=pubdate, is_breaking=is_breaking))
    return news_info


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
# [{"id":"0374cd07e49cc3e3e19616d00caed8facdf3ffa0","title":"Gazprom lukker gassen til \u00d8rsted","url":"http:\/\/nyheder.tv2.dk\/samfund\/2022-05-31-gazprom-lukker-gassen-til-oersted","seq":101123}]
