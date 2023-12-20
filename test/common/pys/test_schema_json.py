from flask import Flask, g
import common.pys.schema_json as schema_json
import unittest
import schema


class CoercerTests(unittest.TestCase):

    def test_coerce_body(self):
        app = Flask("testapp")

        @schema_json.coerce(schema.Schema({'foo': schema.Use(int)}))
        def handler():
            self.assertEqual(g.coerced_body, {'foo': 123})

        with app.test_request_context(json={'foo': '123'}):
            handler()
