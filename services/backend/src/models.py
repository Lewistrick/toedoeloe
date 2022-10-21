from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text("NOW()"), nullable=False)
    modified_at = Column(DateTime, server_default=text("NOW()"), nullable=False)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    detail = Column(Text)
    due_date = Column(DateTime, nullable=False)
    finished = Column(Boolean, server_default=text("FALSE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=text("NOW()"), nullable=False)
    modified_at = Column(DateTime, server_default=text("NOW()"), nullable=False)

    owner = relationship("User")
