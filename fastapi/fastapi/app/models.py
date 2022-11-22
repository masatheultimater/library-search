from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime

class Item(Base):
  __tablename__ = 'items'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False, unique=True)
  description = Column(Text)
  date = Column(DateTime)
  on_offer = Column(Boolean, default=False)