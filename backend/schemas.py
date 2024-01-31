from pydantic import BaseModel,EmailStr


class User(BaseModel):
    email: EmailStr
    password: str

class NewUser(BaseModel):
    email: EmailStr
    password: str
    phone_no: str
    created_at:str
