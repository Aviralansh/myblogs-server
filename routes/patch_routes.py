from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from pydantic_models.models import patchBlogs, verification
from database.db import getDB, MyBlogs, BlogContent
from sqlalchemy.orm import Session
from routes.auth import is_authorized
from datetime import date
from sqlalchemy.exc import IntegrityError
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.patch('/patch')
def patch_Blog(id: str, creds: verification, new_content: patchBlogs, db : Session = Depends(getDB)):

    authorized = is_authorized(creds.username, creds.password)
    
    if not authorized:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Unauthorized")

    my_blog = db.query(MyBlogs).filter(MyBlogs.id==id).first()
    blog_content = db.query(BlogContent).filter(BlogContent.id==id).first()

    print(my_blog.id)
    print(blog_content)

    if not my_blog or not blog_content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with the id Not found")

    update_data = new_content.model_dump(exclude_unset=True)
    print(update_data)
    old_id = id
    new_id = None

    if "description" in update_data:
        my_blog.description = update_data["description"]

    if "topic" in update_data:
        my_blog.topic = update_data["topic"]

    if "title" in update_data:
        new_id = update_data["title"].lower().replace(" ", "-")
        my_blog.id = new_id
        blog_content.id = new_id
        my_blog.title = update_data["title"]


    if "content" in update_data:
        blog_content.content = update_data["content"]

        wordCount = max(1, len(blog_content.content.split()) // 200)
        readtime = f"{wordCount} min read"
        my_blog.readtime = readtime

    db.commit()