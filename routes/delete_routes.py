from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from pydantic_models.models import verification
from database.db import getDB, MyBlogs, BlogContent
from sqlalchemy.orm import Session
from routes.auth import is_authorized
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.delete('/delete-blog/{id}', status_code=status.HTTP_200_OK)
def deleteblog(creds : verification, id: str, db : Session = Depends(getDB) ):

    if not is_authorized(creds.username, creds.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="You're not authorized to use this route"
                            )

    try:
        blog = db.query(MyBlogs).where(MyBlogs.id==id).first()
        content = db.query(BlogContent).where(BlogContent.id==id).first()
        db.delete(blog)
        db.delete(content)

        db.commit()

    except Exception as e:
        db.rollback()
        logger.error(f"Some error occured\n{e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Some error occured"
        )