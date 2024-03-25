from typing import Annotated, List, Optional

from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models, schemas, oauth2
from app.database import get_db


router = APIRouter(prefix="/posts", tags=["Posts"])





@router.get("", response_model=List[schemas.PostResponse])
def get_posts(
    current_user: Annotated[schemas.PostResponse, Depends(oauth2.get_current_user)],
    db: Session = Depends(get_db),
    search: Optional[str] = "",
    limit: int = 10,
    skip: int = 0,
):
    """Get all posts from the postgres database"""

    # PostgreSQL query
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()

    # SQLAlchemy query
    # posts from the user that is logged in only
    # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()

    # posts from all users
    # posts = (
    #     db.query(models.Post)
    #     .filter(models.Post.title.contains(search))
    #     .limit(limit)
    #     .offset(skip)
    #     .all()
    # )

    posts = (
        db.query(models.Post, func.count(models.Vote.posts_id).label("votes"))
        .join(models.Vote, models.Vote.posts_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )

    return posts


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(
    post: schemas.PostCreate,
    current_user: Annotated[int, Depends(oauth2.get_current_user)],
    db: Session = Depends(get_db),
):
    """Create a post and add into the postgres database"""

    # PostgreSQL query
    # cursor.execute(
    #     """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #     (post.title, post.content, post.published),
    # )

    # new_post = cursor.fetchone()
    # connection.commit()
    new_post = models.Post(**post.model_dump(), owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(
    id: int,
    current_user: Annotated[schemas.PostResponse, Depends(oauth2.get_current_user)],
    db: Session = Depends(get_db),
):
    """Get a single post from the database"""

    # PostgreSQL query
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()

    # SQLAlchemy query
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    post = (
        db.query(models.Post, func.count(models.Vote.posts_id).label("votes"))
        .join(models.Vote, models.Vote.posts_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id)
        .first()
    )

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} not found"}

    # Logged in users can only see self-generated posts
    # if post.owner_id is not current_user.id:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Not authorized to perform requested action",
    #     )

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    current_user: Annotated[schemas.Post, Depends(oauth2.get_current_user)],
    db: Session = Depends(get_db),
):
    """deleting a post from the postgress database"""

    # PostgreSQL query
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # connection.commit()

    # SQLAlchemy query
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    if post.owner_id is not current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    if post:
        db.delete(post)
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(
    id: int,
    post: schemas.PostCreate,
    current_user: Annotated[schemas.Post, Depends(oauth2.get_current_user)],
    db: Session = Depends(get_db),
):
    """Update post using the put method"""

    # PostgreSQL Query
    # cursor.execute(
    #     """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #     (post.title, post.content, post.published, (str(id),)),
    # )
    # updated_post = cursor.fetchone()
    # connection.commit()

    # SQLAlchemy Query
    post_query = db.query(models.Post).filter(models.Post.id == id).first()

    if post_query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    if post_query.owner_id is not current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    if post_query:
        for key, value in post.model_dump().items():
            setattr(post_query, key, value)
        db.commit()
        db.refresh(post_query)

    return post_query
