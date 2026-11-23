from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica 

Session = sessionmaker(bind=engine)
session = Session()

