from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Date, Text

Base = declarative_base()

class MyBlogs(Base):
    __tablename__ = "MyBlogs"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    topic = Column(String)
    date = Column(Date)
    readtime = Column(String)

class BlogContent(Base):
    __tablename__ = "BlogContent"

    id = Column(String, primary_key=True, index=True)
    content = Column(Text)
