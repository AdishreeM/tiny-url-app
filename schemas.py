from pydantic import BaseModel

class TokenBase(BaseModel):
    url: str

class TokenCreate(TokenBase):
    pass

class Token(TokenBase):
    id: int
    token: str
    class Config:
        orm_mode = True