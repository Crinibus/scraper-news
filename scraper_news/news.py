from datetime import datetime


class News:
    def __init__(self, title: str, url: str, source: str, id: str = "", seq: int = "", is_breaking: bool = False, time_saved = None) -> None:
        self.title: str = title
        self.url: str = url
        self.id: str = id
        self.seq = seq
        self.source: str = source
        self.is_breaking: bool = is_breaking
        self.time_saved: str = time_saved if time_saved else datetime.today().strftime("%Y-%m-%d - %H:%M:%S")

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "is_breaking": self.is_breaking,
            "seq": self.seq,
            "time_saved": self.time_saved,
        }
