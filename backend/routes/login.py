from fastapi import APIRouter
from schemas import User

router = APIRouter()


@router.post('/login')
async def get_user(user: User):
    return "get user"
