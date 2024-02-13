from databace import Base,engine
from models import UserModel, OrderModel, ProductModel

Base.metadata.create_all(bind=engine)