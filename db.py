
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senhacript = Column('senhacript', String(256))

    credentials = relationship("Credential", back_populates="owner")


class Credential(Base):
    __tablename__ = "Credenciais"
    id = Column('id', Integer,primary_key=True, autoincrement=True)
    site = Column('site', String)
    usuario = Column('usuario', String)
    senhacript = Column('senhacript', String)
    salt = Column('salt', LargeBinary)

    user_id = Column(Integer, ForeignKey('usuarios.id'))
    owner = relationship('Usuario', back_populates="credentials")

Base.metadata.create_all(bind=db)
