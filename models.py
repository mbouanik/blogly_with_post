from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, Relationship, mapped_column

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[str] = mapped_column(Text, default="")

    def __init__(self, **kwargs) -> None:
        super(User, self).__init__(**kwargs)


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    story: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    user = Relationship("User", backref="posts")

    def __init__(self, **kwargs) -> None:
        super(Post, self).__init__(**kwargs)
