from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import get_routes, post_routes, delete_routes, patch_routes
import logging

origins = [
    "http://localhost:3000",      # React/Next.js default
    "http://127.0.0.1:5500",     # Live Server extension default
    "https://yourfrontend.com",  # Production frontend domain
]






logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)



app = FastAPI()
app.include_router(get_routes.router)
app.include_router(post_routes.router)
app.include_router(delete_routes.router)
app.include_router(patch_routes.router)


# 2. Add the middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allows traffic from specific domains
    allow_credentials=True,           # Allows cookies and authentication headers
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],              # Allows all HTTP headers
)
