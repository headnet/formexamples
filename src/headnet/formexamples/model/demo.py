# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope import interface
from zope import schema

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import functions
from sqlalchemy import (Table, Column,
                        Integer, String,
                        Boolean, DateTime,
                        Date, Text, Float,
                        ForeignKey, Sequence,
                        UniqueConstraint,
                        Index)
from sqlalchemy.ext.associationproxy import association_proxy

from base import Base


class IDemo(Interface):
    """
    """
    field1 = schema.TextLine(
                    title=u"Demo field 1",
                    required=True
                    )
    field2 = schema.Bool(
                    title=u"Demo field 2",
                    description=u"Help text",
                    default=False
                    )


class Demo(Base):
    interface.implements(IDemo)
    __tablename__ = "demo"
    __table_args__ = {'mysql_engine':'InnoDB',
                      'mysql_charset':'utf8'}

    row_id = Column(Integer, Sequence(__tablename__ + "_row_id"), primary_key=True)

    field1 = Column(String(500), nullable=False)
    field2 = Column(Boolean, default=False)

    children = relationship("DemoChild",
                              order_by="DemoChild.row_id",
                              backref=backref('parent'))

    created = Column(DateTime, default=functions.now())
    edited = Column(DateTime, onupdate=functions.current_timestamp())
    edited_by = Column(String(50))

