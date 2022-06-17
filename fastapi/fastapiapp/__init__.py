import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def index():
  return { "message": "python-wsgi-function-samples-fastapi" }

@app.get("/hello/{name}")
async def get_name(name: str):
  return { "message": f"Hello {name}, from python-wsgi-function-samples-fastapi" }