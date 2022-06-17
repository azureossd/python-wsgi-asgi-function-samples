from bottle import default_app, route

app = default_app()


@route('/')
def index():
    return { "message": "python-wsgi-function-samples-bottle" }

@route('/hello/<name>')
def index(name):
    return { "message": f"Hello {name}, from python-wsgi-function-samples-bottle." }
