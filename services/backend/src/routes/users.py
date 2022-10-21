from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import User
from src.utils import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user = db.query(User).filter(User.id == current_user.id)
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
