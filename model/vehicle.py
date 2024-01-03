import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, Date, SMALLINT, ForeignKey


class Vehicle(Base):
    __tablename__ = "vehicle"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    type = Column(SMALLINT, nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(SMALLINT)
    route_id = Column(Integer, ForeignKey("route.id"))
    routes = relationship("Route", back_populates="vehicle")
    added_date = Column(Date, default=datetime.datetime)
