from fastapi import FastAPI, Path, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from schemas import Item
app = FastAPI()

items: List[Item] = [
    Item(id=1, name="phone", description="Mobile phone", price=500, quantity=1),
    Item(id=2, name="laptop", description="Gaming laptop", price=1200, quantity=1),
    Item(id=3, name="headphones", description="Noise-cancelling headphones", price=150, quantity=1),
    Item(id=4, name="mouse", description="Wireless mouse", price=25, quantity=1)
]
next_id = len(items) + 1 

@app.get("/items", status_code=status.HTTP_200_OK)
def retrieve_items():
    return items

@app.post("/items", status_code=status.HTTP_201_CREATED)
def add_item(item: Item):
    item.id = next_id
    items.append(item)
    return item

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int = Path(..., gt=0)):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.put("/items/{item_id}")
def edit_item(item_id: int, updated_item: Item):
    for i, item in enumerate(items):
        if item.id == item_id:
            updated_item.id = item_id
            items[i] = updated_item
            return items[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
