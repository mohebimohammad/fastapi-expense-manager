from typing import Optional

from fastapi import status, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base 
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(DateTime)

    def __repr__(self):
        return (f"<Item id={self.id} title='{self.title}' "
                f"description='{self.description}' price={self.price} timestamp={self.timestamp}>")
    

Base.metadata.create_all(bind=engine)

def create_item(title, description, price):
    item = Item(
        title=title, description=description, price=price,
        timestamp=datetime.now()
        )    
    with SessionLocal() as session:
        session = SessionLocal()
        session.add(item)
        session.commit()

def get_item(id: Optional[int] = None):
    with SessionLocal() as session:
        if id:
            item = session.query(Item).filter(Item.id == id).first()
            if item:
                return item
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        else:
            item = session.query(Item).all()

        return item

def delete_item(id):
    with SessionLocal() as session:
        item = session.query(Item).filter(Item.id == id).first()
        if item:
            session.delete(item)
            session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    
def edit_item(id):
    pass