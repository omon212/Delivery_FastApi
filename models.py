from databace import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(70), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('OrderModel', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"


class OrderModel(Base):
    __tablename__ = "orders"
    order_status = (
        ('PENDING', 'PENDING'),
        ('IN_TRANSIT', 'IN_TRANSIT'),
        ('DELIVERED', 'DELIVERED'),
    )
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_statuss = Column(ChoiceType(choices=order_status), default='PENDING')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('UserModel', back_populates='orders')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('ProductModel', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.product_id}>"


class ProductModel(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer, nullable=False)
    orders = relationship('OrderModel', back_populates='product')

    def __repr__(self):
        return f"<Product {self.name}>"
