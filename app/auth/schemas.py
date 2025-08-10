from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: constr(min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True
