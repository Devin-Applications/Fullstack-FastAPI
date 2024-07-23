from fastapi import APIRouter, HTTPException, Path, Body, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.api.v1.endpoints import deps
from backend.app.models.pet import Pet
from backend.app.schemas.pet import PetCreate, PetUpdate, PetInDB
from backend.app.crud.crud_pet import crud_pet

router = APIRouter()

@router.post("/", response_model=PetInDB)
async def create_pet(
    *,
    db: AsyncSession = Depends(deps.get_db),
    pet_in: PetCreate
) -> PetInDB:
    """
    Create a new pet in the system.
    """
    pet = await crud_pet.create(db=db, obj_in=pet_in)
    return pet

@router.get("/{pet_id}", response_model=PetInDB)
async def read_pet(
    *,
    db: AsyncSession = Depends(deps.get_db),
    pet_id: int = Path(..., title="The ID of the pet to get")
) -> PetInDB:
    """
    Get a pet by ID.
    """
    pet = await crud_pet.get(db=db, id=pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.put("/{pet_id}", response_model=PetInDB)
async def update_pet(
    *,
    db: AsyncSession = Depends(deps.get_db),
    pet_id: int = Path(..., title="The ID of the pet to update"),
    pet_in: PetUpdate
) -> PetInDB:
    """
    Update a pet.
    """
    pet = await crud_pet.get(db=db, id=pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    pet = await crud_pet.update(db=db, db_obj=pet, obj_in=pet_in)
    return pet

@router.delete("/{pet_id}", response_model=PetInDB)
async def delete_pet(
    *,
    db: AsyncSession = Depends(deps.get_db),
    pet_id: int = Path(..., title="The ID of the pet to delete")
) -> PetInDB:
    """
    Delete a pet.
    """
    pet = await crud_pet.get(db=db, id=pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    pet = await crud_pet.remove(db=db, id=pet_id)
    return pet
