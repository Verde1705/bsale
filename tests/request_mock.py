import json


class MockResponse():

    def __init__(self, status_code, url, method, body):
        self.request = MockRequest(url, method, body)
        self.status_code = status_code

    def json(self):
        return json.loads(self.request.body)


class MockRequest():

    def __init__(self, url, method, body):
        self.url = url
        self.method = method
        self.body = json.dumps(body)
