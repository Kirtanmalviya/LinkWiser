from fastapi import APIRouter, Depends
from ..config.database import get_db
from sqlalchemy.orm import Session
from ..controllers import userControllers
from ..schemas.userSchemas import UserRegister, UserRegisterResponse, UserLogin, UserLoginResponse

user_routes = APIRouter(
    prefix = "/user",
    tags = ["user"]
)

@user_routes.post("/register", status_code = 201)
def createUser(
    Body: UserRegister, 
    db: Session = Depends(get_db)
):
    
    return userControllers.createUser(Body,db)

@user_routes.post("/login", status_code = 200)
def userLogin(
    Body: UserLogin, 
    db : Session = Depends(get_db)
):
    
    return userControllers.userLogin(Body,db)
