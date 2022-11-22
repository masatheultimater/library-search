from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# postgresql://{user}:{password}@{host}:{port}/{dababase}
engine=create_engine(
  'postgresql://postgres:diamonds@postgres:5432/postgres',
  echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)