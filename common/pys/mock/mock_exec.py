import json


def do_raw_request(hf, rq={}, headers={}):
    default_headers = {"x-forwarded-for": "1.2.3.4, 5.6.7.8",
                       "x-forwarded-proto": "http"}
    eff_headers = {**default_headers, **headers}
    default_rq = {"httpMethod": "GET",
                  "path": "/",
                  "queryStringParameters": {},
                  "headers": eff_headers}
    eff_rq = {**default_rq, **rq}
    return hf(eff_rq, None)


def do_unauth_request(hf, rq={}, headers={}):
    response = do_raw_request(hf, rq=rq, headers=headers)
    try:
        response['body'] = json.loads(response['body'])
    except Exception:
        pass
    return response


def do_request(hf, rq={}, headers={}):
    eff_headers = {
        "authorization": "Bearer validtoken",
        **headers
    }
    return do_unauth_request(hf, rq=rq, headers=eff_headers)


def do_json_request(hf, rq={}, headers={}):
    do_request(
        hf,
        {
            **rq,
            'body': json.dumps(rq['body'])
        },
        {
            'accept': 'application/json',
            'content-type': 'application/json',
            **headers
        }
    )
