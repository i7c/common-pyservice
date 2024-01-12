import aws_lambda_wsgi


def execute_handler(app, event):
    context = aws_lambda_wsgi.environ(
        {
            'httpMethod': 'EXECUTE',
            'queryStringParameters': {},
            'path': '/run',
            'headers': {"x-forwarded-proto": "directevent",
                        "accept": "application/json"},
            **event
        },
        None)

    with app.request_context(context):
        sr = aws_lambda_wsgi.StartResponse()
        output = app(context, sr)
        return sr.response(output)
