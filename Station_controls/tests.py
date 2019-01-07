from django.test import TestCase, Client
from rest_framework.utils import json


class DataRequestTest(TestCase):
    # def test_check_requets_parsing(self):
        # post_data = {"columns": ["Station"]}
        # response = requests.post(url="http://localhost:8000/request_data/", json=json.dumps(post_data))
        # print(response)

        def Setup(self):
            self.c = Client()

        def test_check_request_parsing(self):
            post_data = {
                            "Time": "day",
                            "Station": "Gmina Skawina, Zelczyna",
                            "Columns": ["Stations", "Temperature"]
                        }
            response = self.client.post(path="/request_data/", data=json.dumps(post_data), content_type="application/json", secure=False)
            print(json.loads(response.content))

        def test_check_stations_request(self):
            response = self.client.post(path="/view_stations_available/", secure=False)
            print(json.loads(response.content))

        def test_check_data_request(self):
            response = self.client.post(path="/view_data_available/", secure=False)
            print(json.loads(response.content))