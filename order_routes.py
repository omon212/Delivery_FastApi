from fastapi import APIRouter

order_routher = APIRouter(
    prefix='/order'
)

@order_routher.get('/')
async def order():
    return {'message':'Bu order route sign up sahifasi'}