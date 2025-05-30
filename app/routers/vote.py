from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select, func
from sqlalchemy.orm import selectinload
from ..database import get_session
from ..Schemas import Vote_s
from ..model import User, Vote, Post
from ..oauth2 import get_current_user

router = APIRouter()

@router.post("/vote", status_code= status.HTTP_201_CREATED)
def create_vote(vote: Vote_s, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    post = session.get(Post, vote.post_id) # check whether the post exists
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    vote_query = select(Vote).where(
        Vote.post_id == vote.post_id,
        Vote.user_id == current_user.id
    )
    existing_vote = session.exec(vote_query).first()

    if vote.dir == 1:
        if existing_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User has already voted on this post"
            )
        new_vote = Vote(post_id=vote.post_id, user_id=current_user.id)
        session.add(new_vote)
        session.commit()
        session.refresh(new_vote)
        return {'message': 'Vote added successfully'}
    else:
        if not existing_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist"
            )
        session.delete(existing_vote)
        session.commit()
        return {'message': 'Vote removed successfully'}