from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.database import engine
from app.routers import post, users, auth, vote


# Using alembic for database migration instead of sqlalchemy
# For database migration using sqlalchemy
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """The root of the path operation"""
    return {"message": "Hello World"}


# my_posts = [
#     {"title": "title of post 1", "content": "content of post 1", "id": 1},
#     {"title": "favourite food", "content": "I like seafood", "id": 2},
# ]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i


app.include_router(post.router)
app.include_router(users.router)
app.include_router(vote.router)
app.include_router(auth.router)
