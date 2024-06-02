from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column(String(12), nullable=False)

class Chats(Base):
    __tablename__ = 'chats'
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_tg_id: Mapped[int]

class Messages(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('chats.id'))


class UsersChats(Base):
    __tablename__ = 'users_chat'
    chat_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('chats.id'), primary_key=True)


