import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, Date, Double


class Point(Base):
    __tablename__ = "point"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    location = relationship("Location", back_populates="coordinates")
    added_date = Column(Date, default=datetime.datetime)
