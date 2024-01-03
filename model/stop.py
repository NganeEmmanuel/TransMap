import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey


class Stop(Base):
    __tablename__ = "stop"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey("location.id"))
    location = relationship("Location", back_populates="stops")
    route = relationship("Route", back_populates="stops")
    user = relationship("User", back_populates="recentStops")
    added_date = Column(Date, default=datetime.datetime)
