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

    def get_all(self):
        return self.storage

    def get_one(self, id_):
        for article in self.storage:
            if article['id'] == id_:
                return article
