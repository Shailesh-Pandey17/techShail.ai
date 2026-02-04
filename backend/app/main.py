from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "env": settings.ENV}

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    return {"db": "connected"}
