from utils.DateFormat import DateFormat


class Ticket():
    def __init__(self, id, title=None, author=None, publication_date=None, content=None) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'publication_date': DateFormat.convert_date(self.publication_date),
            'content': self.content,
        }
