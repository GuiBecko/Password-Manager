from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///database.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senhacript = Column('senhacript', String)
    senha = Column('senha', String)

Base.metadata.create_all(bind=db)

#ususarrio = session.query(Usuario).delete()
#session.commit()