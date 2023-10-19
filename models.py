from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, Relationship, mapped_column
from datetime import datetime

db = SQLAlchemy()
DEFAULT_IMG = "https://wallpapercave.com/wp/wp12696574.jpg"


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[Date] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow()
    )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    def __init__(self, **kwargs) -> None:
        super(Post, self).__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Post: {self.title}>"


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String, default=DEFAULT_IMG)

    posts: Mapped[Post] = Relationship("Post", backref="users", cascade="all, delete")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __init__(self, **kwargs) -> None:
        super(User, self).__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<User: {self.full_name}>"
