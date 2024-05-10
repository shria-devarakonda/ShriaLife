# todo: flesh out and make it non ai generated and more specific to usecase (db instance, creds in the constants file etc)

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection string
DATABASE_URL = 'postgresql://postgres:supersecret@ReadOnlyMemory:5432/BrainBase'

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session maker
Session = sessionmaker(bind=engine)

# Create a base class
Base = declarative_base()

# Define a sample table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
session = Session()

# Insert a new record
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

# Close the session
session.close()
