from fastapi import APIRouter, Request
from fastapi import Depends, HTTPException, status
from pydantic_models.models import addPost, verification
from database.db import getDB, MyBlogs, BlogContent
from sqlalchemy.orm import Session
from routes.auth import is_authorized
from datetime import date
from sqlalchemy.exc import IntegrityError
from middleware.middleware import limiter
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


#### ROUTE ONLY FOR TESTING

@router.post('/check_pswd')
@limiter.limit("3/day")
def addBlog(username: str, password: str, request: Request):

    authorized = is_authorized(username, password)

    if not authorized:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Unauthorized")

    return {"authorised"}

#---------------------------------------------------------------------------------------------------------------------------------
@router.post('/add_blog', status_code=status.HTTP_201_CREATED)
def addBlog(creds : verification, postContent : addPost, db : Session = Depends(getDB)):

#-----------------------------auth-------------------------------------

    authorized = is_authorized(creds.username, creds.password)

    if not authorized:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Unauthorized")

    
    id = postContent.title.lower().replace(" ", "-")


    #calculate readtime:
    wordCount = max(1, len(postContent.content.split()) // 200)
    readtime = f"{wordCount} min read"


    try:
        db.add(MyBlogs(id=id, 
                       title=postContent.title,
                       description=postContent.description,
                       topic=postContent.topic,
                       date=date.today(),
                       readtime=readtime))

        db.add(BlogContent(id=id,
                           content=postContent.content))

        db.commit()

    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="A blog post with same ID already exist")

    except Exception as e:
        db.rollback()
        logger.error(f"{e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Unexpected error occured')