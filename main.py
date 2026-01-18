from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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

# Home page route
@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", context={"posts": posts, "title": "Home"},
    )   

# Single blog post page route
@app.get("/posts/{post_id}", include_in_schema=False)
def single_post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(
                request, "post.html", context={"post": post, "title": title},
            )   
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found!")

# API route to get all posts
@app.get("/api/posts")
def get_posts():
    return posts

# API route to get a single post by ID
@app.get("/api/posts/{post_id}")
def get_posts(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post not found!")