from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Stock(Base):
    __tablename__= "Acoes"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32) unique=True, nullable=False)
    description = Column(String(256))
    status = Column(Boolean)
    price_creation_date = Column(Date, ForeignKey("Cotacoes.creation_date")
    price_update_date = Column(Date, ForeignKey("Cotacoes.update_date")

class Stock_Price(Base):
    __tablename__ = "Cotacoes"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    stock_id = Column(Integer, ForeignKey("Acoes.id"))
    value = Column(Float(precision=4))
    creation_date = Column(Date)
    update_date = Column(Date)
