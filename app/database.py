from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# import psycopg2
# from psycopg2.extras import RealDictCursor


SQLALCHEMY_DATABASE_URL = f"{settings.database_url}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    """Connecting to the database using SQLAlchemy"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Connecting to the PostgreSQL database using Psycopg2
# try:
#     connection = psycopg2.connect(
#         host="localhost",
#         database="fastapi",
#         user="postgres",
#         password=863051,
#         cursor_factory=RealDictCursor,
#     )
#     cursor = connection.cursor()
#     print("Database connection was successful")

# except (psycopg2.Error, psycopg2.OperationalError) as error:
#     print("Connection to database failed")
#     print(f"Error: {error}")

# finally:
#     if connection:
#         connection.close()
