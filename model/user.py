import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    stop_id = Column(Integer, ForeignKey("stop.id"), nullable=True)
    recentStops = relationship("Stop", back_populates="user")
    authority_id = Column(Integer, ForeignKey("authority.id"), nullable=True)
    authorities = relationship("Authority", back_populates="user")
    date_joined = Column(Date, default=datetime.datetime.now())
    updated_date = Column(Date, default=datetime.datetime.now())

