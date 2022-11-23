class ArticleDB:
    storage = [
        {
            "id": 1,
            "title": "title1",
            "text": """
                textTEXTtext textTEXTtext,textTEXTtext. textTEXTtext-textTEXTtext
                """
        },
        {
            "id": 2,
            "title": "title2",
            "text": """
                textTEXTtext textTEXTtext,textTEXTtext. textTEXTtext-textTEXTtext
                """
        },
        {
            "id": 3,
            "title": "title3",
            "text": """
                textTEXTtext textTEXTtext,textTEXTtext. textTEXTtext-textTEXTtext
                """
        }
    ]
    last_id = 3

    def get_all(self):
        return self.storage

    def get_one(self, id_):
        for article in self.storage:
            if article['id'] == id_:
                return article

    def create(self, title, text):
        self.last_id += 1
        new_article = {
            "id": self.last_id,
            "title": title,
            "text": text
        }
        self.storage.append(new_article)
        return new_article
