from fastapi import FastAPI, Path, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from database import delete_item, get_item, create_item, edit_item

app = FastAPI()

@app.get("/items", status_code=status.HTTP_200_OK)
def retrieve_items():
    return get_item()

@app.post("/items", status_code=status.HTTP_201_CREATED)
def add_item(title, description, price):
    create_item(title, description, price)

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int = Path(..., gt=0)):
    return get_item(item_id)

# add put operation here

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: int):
    delete_item(item_id)
    