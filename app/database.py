from sqlalchemy.orm import declarative_base


# class SqlAlchemyBase(DeclarativeBase):
#     ...

SqlAlchemyBase = declarative_base()


# engine = create_engine(settings.postgres.sqlalchemy_url)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)