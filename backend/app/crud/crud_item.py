from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional

from backend.app.models.item import Item
from backend.app.schemas.item import ItemCreate, ItemUpdate

class CRUDItem:
    def create_item(self, db: Session, item: ItemCreate) -> Item:
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_item(self, db: Session, item_id: UUID) -> Optional[Item]:
        return db.query(Item).filter(Item.id == item_id).first()

    def get_items(self, db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        return db.query(Item).offset(skip).limit(limit).all()

    def update_item(self, db: Session, item_id: UUID, item: ItemUpdate) -> Optional[Item]:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            for key, value in item.dict().items():
                setattr(db_item, key, value)
            db.commit()
            db.refresh(db_item)
        return db_item

    def delete_item(self, db: Session, item_id: UUID) -> Optional[Item]:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
        return db_item

crud_item = CRUDItem()
