import re
from flask import abort, g, request


def deny(req) -> bool:
    return False


class MockAuthInterceptor(object):
    auth_header_payload = re.compile("Bearer[\s]+")

    def init_app(self, app):
        def interceptor():
            allow_fn = app.extensions.get('unsecure_routes', deny)
            try:
                if allow_fn(request):
                    return
                if request.method == "OPTIONS":
                    return
                auth_header = request.headers.get('authorization')
                if not auth_header or auth_header.isspace():
                    abort(401)
                if not auth_header.startswith('Bearer'):
                    abort(401)
                payload = MockAuthInterceptor.auth_header_payload.sub("", auth_header)
                if not payload == "validtoken":
                    abort(401)
                g.auth_identity = {"sub": "1234"}
            except Exception:
                abort(401)

        app.before_request(interceptor)
