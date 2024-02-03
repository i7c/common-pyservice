from flask import Flask, g
from werkzeug.exceptions import BadRequest, InternalServerError
import common.pys.schema_json as schema_json
import schema
import unittest


class CoercerTests(unittest.TestCase):

    def test_coerce_and_externalize_if_schemas_match(self):
        app = Flask("testapp")

        @schema_json.coerce(schema.Schema({'foo': schema.Use(int)}))
        @schema_json.externalize(schema.Schema({'bar': schema.Use(str)}))
        def handler():
            self.assertEqual(g.coerced_body, {'foo': 123})
            return {'bar': 124}

        with app.test_request_context(json={'foo': '123'}):
            result = handler()
            self.assertEqual(result, {'bar': '124'})

    def test_coerce_with_problem_in_schema(self):
        app = Flask("testapp")

        @schema_json.coerce(schema.Schema({'foo': schema.Use(int)}))
        def handler():
            pass

        with app.test_request_context(json={'bar': 'notconforming'}):
            with self.assertRaises(BadRequest):
                handler()

    def test_externalize_with_problem_in_schema(self):
        app = Flask("testapp")

        @schema_json.externalize(schema.Schema(str))
        def handler():
            return 10

        with app.test_request_context():
            with self.assertRaises(InternalServerError):
                handler()
