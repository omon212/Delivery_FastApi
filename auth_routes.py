from fastapi.exceptions import HTTPException
from fastapi import APIRouter, status
from schemas import Signupmodel
from databace import session, engine
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

auth_routher = APIRouter()
session = session(bind=engine)


@auth_routher.get('/')
async def signup():
    return {'message': 'Bu auth route sign up sahifasi'}


@auth_routher.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: Signupmodel):
    print('ishladi')
    db_email = session.query(UserModel).filter(UserModel.email == user.email).first()
    print(db_email)
    if db_email is not None:
        print('Bu email allaqachon ro`yxatdan o`tilgan')
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Bu email allaqachon ro`yxatdan o`tilgan')

    dp_username = session.query(UserModel).filter(UserModel.username == user.username).first()

    if dp_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='Bu username allaqachon ro`yxatdan o`tilgan')

    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active
    )
    session.add(new_user)
    session.commit()
    return new_user
