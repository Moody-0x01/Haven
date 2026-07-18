from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from hapi import Haven
import requests_cache

app = FastAPI()
haven = Haven()
haven.sfw_only()
haven.set_resolution(1920, 1080)
requests_cache.install_cache('wallhaven_cache', backend='sqlite', expire_after=300)


@app.get("/", response_class=HTMLResponse)
def get_ui():
    with open("./views/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/imIlucky")
async def lucky(limit: int = Query(default=10, ge=1, le=100)):
    return haven.bulk_search("", limit)

@app.get("/search")
async def search(q: str = "", limit: int = Query(default=10, ge=1, le=100)):
    return haven.bulk_search(q, limit)

@app.get("/trending")
async def trending(q: str, limit: int = Query(default=10, ge=1, le=100)):
    return haven.bulk_search_trending(q, limit)