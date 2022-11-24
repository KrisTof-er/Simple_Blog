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

    def update(self, id_, title, text):
        updated_article = {
            "id": id_,
            "title": title,
            "text": text
        }
        for article_number in range(len(self.storage)):
            if self.storage[article_number].get("id") == id_:
                self.storage[article_number] = updated_article
        return updated_article

    def delete(self, id_):
        self.storage = [article for article in self.storage if article["id"] != id_]
