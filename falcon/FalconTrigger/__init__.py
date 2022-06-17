import azure.functions as func
from falconapp import app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app).handle(req, context)
