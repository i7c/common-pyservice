import json


def do_request(hf, rq={}, headers={}):
    default_headers = {"authorization": "Bearer validtoken",
                       "x-forwarded-for": "1.2.3.4, 189.110.31.110, 3.2.3.2",
                       "x-forwarded-proto": "http"}
    eff_headers = {**default_headers, **headers}
    default_rq = {"httpMethod": "GET",
                  "path": "/",
                  "queryStringParameters": {},
                  "headers": eff_headers}
    eff_rq = {**default_rq, **rq}
    return hf(eff_rq, None)


def do_json_request(hf, rq={}, headers={}):
    response = do_request(hf, rq=rq, headers=headers)
    response['body'] = json.loads(response['body'])
