#!/usr/bin/python3
"""add new data to database using sqlalchemy"""

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Louisiana = State("Louisiana")
    session.add(Louisiana)
    session.commit()

    result = session.query(State).filter(State.name == 'Louisiana').first()
    print(result.id)
