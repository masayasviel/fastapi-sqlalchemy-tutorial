from fastapi import FastAPI, HTTPException
from sqlalchemy import select
from pydantic import BaseModel
from db import SessionDep
from models import User, Post

app = FastAPI()


class PostCreate(BaseModel):
    user_id: int
    contents: str


class PostResponse(BaseModel):
    user_id: int
    contents: str
    user_name: str


@app.post("/top", response_model=PostResponse)
def create_post(post_data: PostCreate, db: SessionDep):
    user = db.query(User).filter(User.id == post_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_post = Post(user_id=post_data.user_id, contents=post_data.contents)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    stmt = (
        select(Post.user_id.label("user_id"), Post.contents.label("contents"), User.name.label("user_name"))
        .join(User, Post.user_id == User.id)
        .where(Post.id == new_post.id)
    )
    result = db.execute(stmt).first()
    if result is None:
        raise HTTPException(status_code=500, detail="Post join failed")
    return PostResponse(
        user_id=result.user_id,
        contents=result.contents,
        user_name=result.user_name
    )
