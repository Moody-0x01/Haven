from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from hapi import Haven

app = FastAPI()
haven = Haven()


@app.get("/", response_class=HTMLResponse)
def get_ui():
    with open("./views/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/imIlucky")
async def lucky(limit: int = Query(default=10, ge=1, le=100)):
    return haven.bulk_search("", limit)

@app.get("/search")
async def search(q: str = "", limit: int = Query(default=1, ge=1, le=100)):
    return haven.bulk_search(q, limit)
