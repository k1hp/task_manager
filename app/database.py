from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, MappedColumn, Mapped, relationship


class SqlAlchemyBase(DeclarativeBase):
    ...


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id: Mapped[int] = MappedColumn(autoincrement=True, primary_key=True)
    name: str = MappedColumn(autoincrement=True, nullable=False)
    password: str = MappedColumn(autoincrement=True, nullable=False)
    email: str = MappedColumn(autoincrement=True, nullable=False)
    tasks: Mapped[list["Task"]] = relationship(back_populates="user")


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'
    id: Mapped[int] = MappedColumn(autoincrement=True, primary_key=True)
    name: Mapped[str] = MappedColumn(nullable=False)
    user_id: Mapped[int] = MappedColumn(ForeignKey('users.id'), nullable=False)
    user: Mapped[User] = relationship(back_populates='tasks')
