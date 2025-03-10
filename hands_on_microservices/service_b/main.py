from fastapi import FastAPI
from typing import Annotated

from fastapi import Depends, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select



app = FastAPI()


@app.get("/data")
async def get_data():
    return {"message": "Hello from Service B!"}
