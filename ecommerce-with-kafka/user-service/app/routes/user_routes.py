from typing import Annotated
from fastapi import APIRouter, Depends
from app.controllers.crud_user import user_add
from app.models.user_models import UserModel
router = APIRouter()

@router.get("/users")
def get_user():
    ...

@router.post("/add_user")
def add_user(user: Annotated[UserModel, Depends(user_add)]):
    return user

@router.put("/update_user")
def update_user():
    ...
    
@router.delete("/delete_user")
def delete_user():
    ...