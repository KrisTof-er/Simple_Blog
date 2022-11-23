class PostDB:
    storage = [
        {
            "id": 1,
            "title": "title1",
            "text": """
            textTEXTtext textTEXTtext,textTEXTtext. textTEXTtext-textTEXTtext
            """
        }
    ]

    def get_all(self):
        return self.storage
