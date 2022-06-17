from typing import List

from pydantic import BaseModel
from sqlalchemy import table


class TablesBase(BaseModel):
    table_project: str
    table_dataset: str
    table_name: str


class TablesCreate(TablesBase):
    pass
