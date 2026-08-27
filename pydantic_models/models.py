from pydantic import BaseModel
import datetime

class getBlogsResponse(BaseModel):
    id : str
    title : str
    description : str
    topic : str
    date : datetime.date
    readtime : str

class getBlogContentResponse(BaseModel):
    id : str
    title : str
    description : str
    topic : str
    date : datetime.date
    readtime : str
    content : str

class verification(BaseModel):
    username : str
    password : str

class addPost(BaseModel):
    title : str
    description : str
    topic : str
    content : str
    
class patchBlogs(BaseModel):
    title : str | None = None
    description : str | None = None
    topic : str | None = None
    content : str | None = None