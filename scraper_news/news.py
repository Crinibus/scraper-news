from datetime import datetime


class News:
    def __init__(self, title: str, url: str, id: str = "", seq: int = "", is_breaking: bool = False) -> None:
        self.title: str = title
        self.url: str = url
        self.id: str = id
        self.seq = seq
        self.is_breaking: bool = is_breaking

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "is_breaking": self.is_breaking,
            "seq": self.seq,
            "time_saved": datetime.today().strftime("%Y-%m-%d - %H:%M:%S"),
        }
