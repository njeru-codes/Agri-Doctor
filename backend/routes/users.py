from fastapi import APIRouter , Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemas import NewUser
from sqlalchemy.orm import Session
from database import get_db



router = APIRouter()


@router.post('/new-user')
async def get_user(db:Session =Depends(get_db),  user_credentials: OAuth2PasswordRequestForm=Depends()):
    return "new user"

@router.get('/user')
async def get_user(new_user: NewUser):
    return "new user"


