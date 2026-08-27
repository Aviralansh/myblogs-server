from sqlalchemy.orm import sessionmaker
import database.db_models
from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

load_dotenv()



DB_URL = os.getenv('DB_URL')
logging.info(f"connecting to DB... {DB_URL}")


try:
    engine = create_engine(DB_URL)
    session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

except RuntimeError:
    logging.warning("Some Error Occured")
    logging.info("Exiting...")
    exit()


database.db_models.Base.metadata.create_all(bind=engine)
MyBlogs = database.db_models.MyBlogs
BlogContent = database.db_models.BlogContent

# -----------------------------------------DB Session
def getDB():
    db = session()
    logging.info("Session Created")
    try:
        yield db
    finally:
        db.close()