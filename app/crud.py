import random
import string

from sqlalchemy.orm import Session

from app import models


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def create_short_url(db: Session, original_url: str):
    short_code = generate_short_code()

    # Ensure the generated short code is unique
    while db.query(models.URL).filter(
        models.URL.short_code == short_code
    ).first():
        short_code = generate_short_code()

    url = models.URL(
        original_url=original_url,
        short_code=short_code
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url


def get_original_url(db: Session, short_code: str):
    return db.query(models.URL).filter(
        models.URL.short_code == short_code
    ).first()