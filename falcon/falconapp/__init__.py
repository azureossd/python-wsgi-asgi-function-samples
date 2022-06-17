import falcon

app = falcon.API()

class IndexResource:
    def on_get(self, req, resp):
        """Handle GET requests."""
        index = {
            'message': 'python-wsgi-function-samples-falcon',
        }

        resp.media = index

app.add_route('/', IndexResource())
