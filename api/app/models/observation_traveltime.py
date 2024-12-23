from app.db.sqlalchemy_db import SCHEMA_NAME, Base
from sqlalchemy.dialects.postgresql.base import TIMESTAMP
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.dialects.postgresql.ranges import TSTZRANGE
from sqlalchemy.sql.schema import Column, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, Text


class ObservationTravelTime(Base):
    __tablename__ = "Observation_traveltime"

    id = Column(Integer)
    self_link = Column("@iot.selfLink", Text)
    featuresofinterest_navigation_link = Column(
        "FeatureOfInterest@iot.navigationLink", Text
    )
    datastream_navigation_link = Column("Datastream@iot.navigationLink", Text)
    commit_navigation_link = Column("Commit@iot.navigationLink", Text)
    phenomenon_time = Column("phenomenonTime", TSTZRANGE)
    result_time = Column("resultTime", TIMESTAMP, nullable=False)
    result = Column(JSON)
    result_string = Column("resultString", Text)
    result_number = Column("resultNumber", Float)
    result_boolean = Column("resultBoolean", Boolean)
    result_json = Column("resultJSON", JSON)
    result_quality = Column("resultQuality", JSON)
    valid_time = Column("validTime", TSTZRANGE)
    parameters = Column(JSON)
    datastream_id = Column(Integer)
    featuresofinterest_id = Column(Integer)
    commit_id = Column(Integer)

    featuresofinterest = Column("FeaturesOfInterest")
    datastream = Column("Datastream")
    commit = Column("Commit")
    system_time_validity = Column("systemTimeValidity", TSTZRANGE)

    __table_args__ = (
        PrimaryKeyConstraint(id, system_time_validity),
        {"schema": SCHEMA_NAME},
    )
