# coding: utf-8
from sqlalchemy import Column, Integer, SmallInteger, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Penguin(Base):
    __tablename__ = 'penguins'

    ID = Column(Integer, primary_key=True)
    Username = Column(String(12), nullable=False, unique=True)
    Nickname = Column(String(16), nullable=False)
    Password = Column(String(255), nullable=False)
    LoginKey = Column(String(32), nullable=False)
    Email = Column(String(254), nullable=False)
    RegistrationDate = Column(Integer, nullable=False)
    LastLogin = Column(Integer, nullable=False)
    LastLogout = Column(Integer, nullable=False)
    Moderator = Column(Integer, nullable=False, server_default=text("'0'"))
    Stripes = Column(Integer, nullable=False, server_default=text("'1'"))
    SafeChat = Column(Integer, nullable=False, server_default=text("'0'"))
    Inventory = Column(Text, nullable=False)
    Coins = Column(Integer, nullable=False, server_default=text("'500'"))
    Igloo = Column(Integer, nullable=False)
    Igloos = Column(Text, nullable=False)
    Furniture = Column(Text, nullable=False)
    Color = Column(Integer, nullable=False, server_default=text("'1'"))
    Head = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Face = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Neck = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Body = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Hand = Column(Integer, nullable=False, server_default=text("'0'"))
    Feet = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Photo = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Flag = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    Walking = Column(Integer, nullable=False, server_default=text("'0'"))
    Banned = Column(String(20), nullable=False, server_default=text("'0'"))
    BanCount = Column(String(20), nullable=False, server_default=text("'0'"))
    Online = Column(Integer, nullable=False, server_default=text("'0'"))
    CurrentServer = Column(Integer, nullable=False, server_default=text("'0'"))
    Stamps = Column(Text, nullable=False)
    StampBook = Column(String(150), nullable=False, server_default=text("'1%1%-1%1'"))
    EPF = Column(String(9), nullable=False, server_default=text("'0,0,0'"))
    FieldStatus = Column(String(1), nullable=False, server_default=text("'0'"))
    PartyOpStatus = Column(String(1), nullable=False, server_default=text("'0'"))
    Buddies = Column(Text, nullable=False)
    Ignores = Column(Text, nullable=False)
    MinutesPlayed = Column(Integer, nullable=False)
    firstTime = Column(Integer, nullable=False, server_default=text("'1'"))
    approved = Column(Integer, nullable=False, server_default=text("'0'"))
    denied = Column(Integer, nullable=False, server_default=text("'0'"))
    IP = Column(Text, nullable=False)
    LoginIPs = Column(Text, nullable=False)
    Notes = Column(Text, nullable=False)
    CPRIP = Column(Integer, nullable=False, server_default=text("'0'"))