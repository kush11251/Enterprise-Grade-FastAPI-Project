from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'sqlite:///example.db'
engine = create_engine(db_url)
db = sessionmaker(bind=engine)()