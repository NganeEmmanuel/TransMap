from Database.database import Base, engine
import user
import point
import location
import stop
import route
import vehicle
Base.metadata.create_all(engine)