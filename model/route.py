import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, Date, Double, ForeignKey


class Route(Base):
    __tablename__ = "route"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    start = Column(Integer, nullable=False)  # todo into persisting the object Stop rather than the id
    end = Column(Integer, nullable=False)  # todo into persisting the object Stop rather than the id
    distance = Column(Double)
    fare = Column(Double)
    stop_id = Column(Integer, ForeignKey("stop.id"))
    stops = relationship("Stop", back_populates="route")
    vehicle = relationship("Vehicle", back_populates="routes")
    added_date = Column(Date, default=datetime.datetime)
