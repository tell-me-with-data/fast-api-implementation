from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .database import Base


class Tables(Base):
    __tablename__ = "tbl_table"
    table_id = Column(Integer, primary_key=True, index=True)
    table_project = Column(String)
    table_dataset = Column(String)
    table_name = Column(String, index=True)
    table_columns = relationship("Columns", back_populates="table_id")


class Columns(Base):
    __tablename__ = "tbl_column"
    column_id = Column(Integer, primary_key=True, index=True)
    column_name = Column(String)
    column_type = Column(String)
    column_length = Column(String)
    column_precision = Column(Integer)
    column_scale = Column(Integer)
    table_id = Column(Integer, ForeignKey("tbl_table.table_id"))
