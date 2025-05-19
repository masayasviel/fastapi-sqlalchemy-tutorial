from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    contents = Column(Text, nullable=False)

    user = relationship("User", back_populates="posts")
