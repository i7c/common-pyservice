import requests


class RequestsDiplomat(object):

    def __init__(self, base_url='http://localhost:8080'):
        self.base_url = base_url
        self.session = requests.Session()
        self.mocks = {}

    def mock(self, method='GET', url='/', response={}):
        self.mocks["{}|{}".format(method, url)] = response

    def req(self, method='GET', url='/', data=None, headers={}, reqschema=None, respschema=None):
        if reqschema:
            reqschema.validate()

        if len(self.mocks) > 0:
            response_payload = self.mocks["{}: {}".format(method, url)]
        else:
            r = requests.Request(
                method,
                url,
                data=data,
                headers={
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    **headers,
                }).prepare()
            response = self.session.send(r)
            response_payload = response.json()

        if respschema:
            respschema.validate(response_payload)
        return response_payload
