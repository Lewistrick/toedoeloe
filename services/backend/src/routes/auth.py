from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from src.config import settings
from src.database import get_db
from src.models import User
from src.schemas.users import UserCreate
from src.utils import check_password, create_access_token, hash_password

router = APIRouter(tags=["Authentication"])


@router.post("/register")
async def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    # check if user already exists
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this name already exists",
        )

    # hash the password
    user.password = hash_password(user.password)

    # create the user
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login")
async def login(
    user: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    # get the user
    db_user = db.query(User).filter(User.username == user.username).first()

    # check if the user exists
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # check if the password is correct
    if not check_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )

    # generate a jwt token
    token = create_access_token(
        data={"sub": db_user.username},
        expires_delta=timedelta(minutes=settings.access_token_expire_minutes),
    )

    # create a response with a cookie
    response = JSONResponse(
        content={
            "access_token": token,
            "token_type": "bearer",
        }
    )
    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        max_age=settings.access_token_expire_minutes * 60,
        expires=settings.access_token_expire_minutes * 60,
        samesite="lax",
        secure=True,
    )

    return response


@router.post("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logged out"})
    response.delete_cookie(key="access_token")
    return response
