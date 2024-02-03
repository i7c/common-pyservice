from flask import Flask
import aws_lambda_wsgi
import common.pys.auth.cognito as cognito
import common.pys.mock.mock_authentication as auth
import unittest


class CoercerTests(unittest.TestCase):

    def test_interceptor_checks_for_group(self):
        app = Flask("testapp")
        auth.MockAuthInterceptor().init_app(app)

        @app.route('/')
        @cognito.requires_group("foogroup")
        def handler():
            return {}

        with app.test_request_context():
            response = aws_lambda_wsgi.response(app, {
                'httpMethod': 'GET',
                'queryStringParameters': {},
                'path': '/',
                'headers': {"x-forwarded-proto": "http"},
            }, None)
            self.assertEqual(response['statusCode'], 401)

            response = aws_lambda_wsgi.response(app, {
                'httpMethod': 'GET',
                'queryStringParameters': {},
                'path': '/',
                'headers': {"x-forwarded-proto": "http",
                            "Authorization":  'Bearer {"cognito:groups": "foogroup"}'},
            }, None)
            self.assertEqual(response['statusCode'], 200)
