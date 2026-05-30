from fastapi import FastAPI, Path, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    id: int | None = None
    description: str
    amount: int

expenses: List[Expense] = [
    Expense(id=1, description="phone", amount=500),
    Expense(id=2, description="dinner", amount=50),
    Expense(id=3, description="water", amount=2)
]

next_id = len(expenses) + 1 

@app.get("/expenses", status_code=status.HTTP_200_OK)
def retrieve_expenses():
    return expenses

@app.post("/expenses", status_code=status.HTTP_201_CREATED)
def add_expense(expense: Expense):
    global next_id
    new_expense = expense.model_copy(update={"id": next_id})
    expenses.append(new_expense)
    next_id += 1
    return new_expense

@app.get("/expenses/{item_id}")
def get_expense_by_id(item_id: int = Path(..., gt=0)):
    for expense in expenses:
        if expense.id == item_id:
            return expense
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.put("/expenses/{item_id}")
def edit_expense(item_id: int, updated_expense: Expense):
    for i, expense in enumerate(expenses):
        if expense.id == item_id:
            expenses[i] = Expense(
                id=item_id,
                description=updated_expense.description,
                amount=updated_expense.amount
            )

            return JSONResponse(content="expense updated", status_code=status.HTTP_202_ACCEPTED)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")

@app.delete("/expenses/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_expense(item_id: int):
    for i, expense in enumerate(expenses):
        if expense.id == item_id:
            expenses.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
