#!/usr/bin/python3
"""prints the first state object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            user, password, database_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(State).first()
        if result is not None:
            print('{}: {}'.format(result.id, result.name))
        else:
            print('Nothing')
