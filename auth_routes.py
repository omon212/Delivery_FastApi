from fastapi import APIRouter

auth_routher = APIRouter(
    prefix='/auth'
)

@auth_routher.get('/')
async def signup():
    return {'message':'Bu auth route sign up sahifasi'}