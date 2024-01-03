import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, Date, String, ForeignKey


class Location(Base):
    __tablename__ = "location"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    point_id = Column(Integer, ForeignKey("point.id"))
    coordinates = relationship("Point", back_populates="location")
    stops = relationship("Stop", back_populates="location")
    added_date = Column(Date, default=datetime.datetime)
