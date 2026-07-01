from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_CONFIG

DATABASE_URL =  (
    f"postgresql+psycopg2://"
    f"{DB_CONFIG['user']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['dbname']}"
)

engine = create_engine(DATADASE_URL)

Session = sessionmaker(bind=engine)

def get_session():
    return Session()
    