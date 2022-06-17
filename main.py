from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Table(BaseModel):
    table_name: str
    table_database: str
    table_project: str


class TableList(BaseModel):
    table_list: List[Table]


@app.get("/table")
async def index_table(table_list: TableList):
    return table_list


@app.get("/table/{table_name}")
async def index_table_name(table_name: str):
    return {"table": table_name}
