from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Jay Tusar",
        "title": "Working with FastAPI",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "January 15, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "January 16, 2026",
    },
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", context={"posts": posts, "title": "Home"},
                                      )   

@app.get("/api/posts")
def get_posts():
    return posts

