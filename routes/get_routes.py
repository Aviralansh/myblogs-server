from fastapi import APIRouter
from pydantic_models.models import getBlogsResponse, getBlogContentResponse
from fastapi import Depends, HTTPException, status
from database.db import getDB, MyBlogs, BlogContent
from sqlalchemy.orm import Session
from typing import cast
import logging

logger = logging.getLogger(__name__)

router = APIRouter()



@router.get('/')
def default() -> dict:
    return {
        'health' : 'Good'
    }

@router.get('/blogs')
def get_blogs(db : Session = Depends(getDB)) -> list[getBlogsResponse]:
        
    queryResult = db.query(MyBlogs).all()
    logger.info(f"List length: {len(list(queryResult))}")

    if not queryResult:
        logger.warning(f"Empty query result /blogs : {queryResult}")
        raise HTTPException(
            status_code=404,
            detail="Item Not Found"
        )

    return list(queryResult)


@router.get('/blog/{id}')
def getBlogContent(id: str, db : Session = Depends(getDB)) -> getBlogContentResponse:
    queryResult = db.query(MyBlogs.id,
                           MyBlogs.title,
                           MyBlogs.description,
                           MyBlogs.topic,
                           MyBlogs.date,
                           MyBlogs.readtime,
                           BlogContent.content
                           ).join(BlogContent, MyBlogs.id == BlogContent.id).filter(BlogContent.id==id.lower()).first()
    if not queryResult:
            logging.warning(f"Empty query result /blogs : {queryResult}")
            raise HTTPException(
                status_code=404,
                detail="Item Not Found"
            )
    
    return cast(getBlogContentResponse, queryResult)