#!/usr/bin/python3
"""
list all state objects from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to a MySQL database based on command line arguments
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(user_name, password, db_name),
                           pool_pre_ping=True)
    newsession = sessionmaker(engine)
    with newsession() as session:
        query = session.query(State).order_by(State.id).all()
        for item in query:
            print("{}: {}".format(item.id, item.name))
