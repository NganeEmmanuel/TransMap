from Database.database import session
from model.point import Point
from model.location import Location
from model.stop import Stop
from model.route import Route
from model.vehicle import Vehicle
from model.authority import Authority
from model.user import User


def login(username, password):
    if username and password:
        user = session.query(User).filter(User.username == username).first()
        if user:
            if user.password == password:
                return "success"
            else:
                return "User credentials not valid"
        else:
            return "User credentials not valid"  # User not found
    else:
        return "Please fill all fields"
