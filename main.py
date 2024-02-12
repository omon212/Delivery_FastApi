from fastapi import FastAPI
from auth_routes import auth_routher
from order_routes import order_routher


app = FastAPI()
app.include_router(auth_routher)
app.include_router(order_routher)


@app.get('/')
async def root():
    return {'messsage':'Bu asosiy sahifa'}