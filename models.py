from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class QA(Base):
    __tablename__ = 'qa'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

engine = create_engine('sqlite:///qa.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
