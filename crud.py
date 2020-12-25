from sqlalchemy.orm import Session

from . import models, schemas

def get_url_by_token(db: Session, token: str):
    return db.query(models.Token).filter(models.Token.token == token).first()

def get_token_by_url(db: Session, url: str):
    return db.query(models.Token).filter(models.Token.url == url).first()

def get_tokens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Token).offset(skip).limit(limit).all()

def create_token(db: Session, tokenObj: schemas.TokenCreate):
    new_token = getNewToken(tokenObj.url) # todo: Create token generator
    db_token = models.Token(token=new_token, url=tokenObj.url)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token
