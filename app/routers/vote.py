from typing import Annotated
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app import schemas, oauth2, models
from app.database import get_db


router = APIRouter(prefix="/vote", tags=["Vote"])


@router.post("", status_code=status.HTTP_201_CREATED)
def vote_on_post(
    vote: schemas.Vote,
    current_user: Annotated[schemas.UserOut, Depends(oauth2.get_current_user)],
    db: Session = Depends(get_db),
):
    """the user votes on a post or removes the vote from a post"""


    # Check to see if the post the user will vote on exists
    user_post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not user_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} does not exist")
    
    # Check for the post id and user id to vote
    user_vote = (
        db.query(models.Vote)
        .filter(
            models.Vote.posts_id == vote.post_id, models.Vote.user_id == current_user.id
        )
        .first()
    )

    if vote.dir == 1:
        if user_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with id: {current_user.id} has already voted on a post",
            )

        new_vote = models.Vote(posts_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message": "Successfully added vote"}

    if vote.dir == 0:
        if not user_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist"
            )

        db.delete(user_vote)
        db.commit()

        return {"message": "vote deleted successfully"}
