import datetime

from sqlalchemy.orm import relationship

from Database.database import Base
from sqlalchemy import Column, Integer, Date, SMALLINT
from model.user import User


class Authority(Base):
    __tablename__ = "authority"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    type = Column(SMALLINT, nullable=False, unique=True)
    user = relationship("User", back_populates="authorities")
    added_date = Column(Date, default=datetime)
