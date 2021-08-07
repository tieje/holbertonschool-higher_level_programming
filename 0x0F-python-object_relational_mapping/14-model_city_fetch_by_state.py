#!/usr/bin/python3
"""
list the first state object from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to a MySQL database based on command line arguments
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(user_name, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).all()
    for res in query:
        print("{}: ({}) {}".format(res.State.name, res.City.id, res.city.name))
    session.close()
