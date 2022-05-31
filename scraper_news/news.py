from datetime import datetime


class News:
    def __init__(self, title: str, url: str, id: str, is_breaking: bool) -> None:
        self.title: str = title
        self.url: str = url
        self.id: str = id
        self.is_breaking: bool = is_breaking

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "is_breaking": self.is_breaking,
            "time_saved": datetime.today().strftime("%Y-%m-%d - %H:%M:%S"),
        }
