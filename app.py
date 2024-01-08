from sqlalchemy import String,Integer,Column,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base = declarative_base()

class Member(Base):
    __tablename__='members'
    memberId = Column('memberId',String,primary_key=True,default=generate_uuid,onupdate=generate_uuid)
    memberName = Column('memberName',String)
    memberAge = Column('memberAge',Integer)

    def __init__(self,memberName,memberAge):
        self.memberName = memberName
        self.memberAge = memberAge

def add_member(session,memberName,memberAge):
    existingMember = session.query(Member).filter_by(memberName=memberName).first()
    if existingMember:
        print('Member already exists')  
    else:
        newMember = Member(memberName,memberAge)
        session.add(newMember)
        session.commit()

db_url = 'sqlite:///myDB.db'
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

memberName='Kai'
memberAge = 28
# add_member(session,memberName,memberAge) 
