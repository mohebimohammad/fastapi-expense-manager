from fastapi import FastAPI, Path, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from database import delete_item, get_item, create_item, update_item
from schemas import Item, ItemResponse
app = FastAPI()


@app.get("/items", status_code=status.HTTP_200_OK, response_model=List[ItemResponse])
def retrieve_items():
    return get_item()

@app.post("/items", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
def add_item(item: Item):
    return create_item(item.title, item.description, item.price)

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item_by_id(item_id: int = Path(..., gt=0, description="The ID of the item to get")):
    return get_item(item_id)

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item_by_id(
    item_id: int = Path(..., gt=0, description="The ID of the item to edit"),
    item: Item = None):
    return update_item(
        id=item_id, title=item.title if item else None,
        description = item.description if item else None,
        price = item.price if item else None)

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: int = Path(..., gt=0, description="The ID of the item to delete")):
    delete_item(item_id)
    return None