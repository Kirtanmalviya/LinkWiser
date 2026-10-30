from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..config.auth import hash_password, verify_password
from app.models.userModel import User
from ..schemas.userSchemas import UserRegister, UserLogin # type: ignore

def createUser(Body: UserRegister, db: Session):

    data = Body.model_dump()

    name: str = data.get("name") #type: ignore
    email: str = data.get("email") #type: ignore
    hashed_password: str = hash_password((data.get("password"))) #type: ignore

    query = select(
        User.email
        ).where(
            User.email == email
        )
    user = db.execute(query).one_or_none()

    if user:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, 
            detail = "email already exist"
        )

    new_user = UserRegister(
        name = name,
        email = email,
        password = hashed_password
    )

    db.add(new_user)
    db.refresh(new_user)
    db.commit()

    return new_user

def userLogin(Body: UserLogin, db: Session):
    data = Body.model_dump()

    email = data.get("email")
    password:str = data.get("password") # type: ignore

    query = select(User).where(User.email == email)
    user = db.scalars(query).one_or_none()

    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "wrong credentials try again")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "wrong credentials try again")

    return {
        "message": "success"
    }