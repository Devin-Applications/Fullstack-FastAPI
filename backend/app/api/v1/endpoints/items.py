from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.crud_item import crud_item
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.api.deps import get_db

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item(item_data: ItemCreate, db: Session = Depends(get_db)):
    return crud_item.create_item(db=db, item=item_data)

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: UUID, db: Session = Depends(get_db)):
    db_item = crud_item.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/items/", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_item.get_items(db=db, skip=skip, limit=limit)

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: UUID, item_data: ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud_item.update_item(db=db, item_id=item_id, item=item_data)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: UUID, db: Session = Depends(get_db)):
    db_item = crud_item.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
