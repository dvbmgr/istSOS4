from app.db.sqlalchemy_db import SCHEMA_NAME, Base
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text


class ObservedProperty(Base):
    __tablename__ = "ObservedProperty"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(Integer, primary_key=True)
    self_link = Column("@iot.selfLink", Text)
    datastream_navigation_link = Column("Datastreams@iot.navigationLink", Text)
    commit_navigation_link = Column("Commit@iot.navigationLink", Text)
    name = Column(String(255), unique=True, nullable=False)
    definition = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    properties = Column(JSON)
    commit_id = Column(
        Integer,
        ForeignKey(f"{SCHEMA_NAME}.Commit.id"),
    )
    datastream = relationship("Datastream", back_populates="observedproperty")
    commit = relationship("Commit", back_populates="observedproperty")
