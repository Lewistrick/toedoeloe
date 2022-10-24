from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import desc
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Todo, User
from src.schemas.todos import TodoIn, TodoOut
from src.utils import get_current_user

router = APIRouter(prefix="/todos", tags=["Todos"])


def check_todo_exists(todo) -> bool:
    """Helper function to check if a todo exists"""
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return True


def check_owner(todo, current_user) -> bool:
    """Helper function to check if the current user is the owner of the todo"""
    if todo.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not the owner of this todo",
        )
    return True


@router.get("/", response_model=list[TodoOut])
async def get_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Todo)
        .filter(Todo.user_id == current_user.id)
        .order_by(desc(Todo.due_date))
        .all()
    )


@router.get("/{todo_id}", response_model=TodoOut)
async def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    check_todo_exists(todo)
    check_owner(todo, current_user)

    return todo


@router.post("/", response_model=TodoOut)
async def create_todo(
    todo: TodoIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    print(f"Received todo: {todo}")
    print(f"Details: {todo.dict()}")
    todo = Todo(**todo.dict(), user_id=current_user.id)
    print("Adding")
    db.add(todo)
    print("Committing")
    db.commit()
    print("Refreshing")
    db.refresh(todo)
    print("Returning")
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo_query = db.query(Todo).filter(Todo.id == todo_id)
    todo = todo_query.first()

    check_todo_exists(todo)
    check_owner(todo, current_user)

    todo_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{todo_id}", response_model=TodoOut)
async def update_todo(
    todo_id: int,
    todo_new: TodoIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo_query = db.query(Todo).filter(Todo.id == todo_id)
    todo = todo_query.first()

    check_todo_exists(todo)
    check_owner(todo, current_user)

    todo_dict = todo_new.dict()
    todo_dict["modified_at"] = datetime.now()

    todo_query.update(todo_dict, synchronize_session=False)
    db.commit()

    return todo_query.first()


@router.put("/{todo_id}/toggle_finished", response_model=TodoOut)
async def toggle_finished(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    check_todo_exists(todo)
    check_owner(todo, current_user)

    todo.finished = not todo.finished
    todo.modified_at = datetime.now()

    db.commit()
    db.refresh(todo)
    return todo
