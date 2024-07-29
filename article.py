class Article:
    def __init__(self, title, link, content, publication_date):
        self.title = title
        self.link = link
        self.content = content
        self.publication_date = publication_date

    def to_dict(self):
        return {
            'title': self.title,
            'link': self.link,
            'content': self.content,
            'publication_date': self.publication_date
        }
