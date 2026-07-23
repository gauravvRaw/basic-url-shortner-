from fastapi import FastAPI
from pydantic import BaseModel
from another import add_link, look_up, generate_short_code
from fastapi.responses import RedirectResponse
app = FastAPI()

class Link(BaseModel):
    link: str

@app.get("/{short}")
def redirect(short: str):
    original_link = look_up(short)
    if original_link:
        return RedirectResponse(original_link)
    else:
        return {"error": "Short link not found"}

@app.post("/add")
def add_link_endpoint(url: Link):
    short = generate_short_code(url.link)
    add_link(url.link, short)
    return {"message": "Link added successfully"}