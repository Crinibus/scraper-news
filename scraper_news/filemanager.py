import pathlib
import json


class Filemanager:
    # root path of this repository
    root_path = pathlib.Path(__file__).parent.parent.absolute()
    news_path = f"{root_path}/scraper_news/news.json"
    logging_ini_path = f"{root_path}/scraper_news/logging.ini"
    logfile_path = f"{root_path}/scraper_news/logfile.log"

    @staticmethod
    def read_json(filename: str) -> dict:
        with open(filename, "r", encoding="utf8") as file:
            data = json.load(file)
        return data

    @staticmethod
    def write_json(filename: str, data: dict):
        with open(filename, "w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def get_news_data() -> dict:
        data = Filemanager.read_json(Filemanager.news_path)
        return data

    @staticmethod
    def save_news_data(data: dict) -> None:
        Filemanager.write_json(Filemanager.news_path, data)
