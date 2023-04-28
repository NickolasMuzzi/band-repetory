import os
from googleapiclient.discovery import build


class GoogleSearch():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cse_id = os.getenv('CSE_ID')

    def search(self):

        service = build("customsearch", "v1", developerKey=self.api_key)

        res = service.cse().list(q=self.pesquisa, cx=self.cse_id).execute()

        return res
