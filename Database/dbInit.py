from Database import crud
from Database.database import Base, engine, session
from model import user
from model import authority
from model import point
from model import location
from model import stop
from model import route
from model import vehicle
from model.user import User


def create_tables():
    Base.metadata.create_all(engine)

