from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import engine, Base, SessionLocal
from app import models, schemas, crud

app = FastAPI(
    title="URL Shortener API",
    description="A simple URL Shortener API built using FastAPI and PostgreSQL.",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "URL Shortener API is running successfully!"}


@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(
    request: schemas.URLRequest,
    db: Session = Depends(get_db)
):
    url = crud.create_short_url(db, str(request.long_url))

    return {
        "short_url": f"http://localhost:8000/{url.short_code}"
    }


@app.get("/{short_code}")
def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = crud.get_original_url(db, short_code)

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(url.original_url)