from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def user_registration(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example= 'UrbanUser')]
                    , age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example= '24')]) -> User:
    new_user = User(id= users[-1].id + 1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def user_update(user_id: int, username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example= 'UrbanUser')]
                    , age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example= '24')]) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        for user in users:
            if user.id == user_id:
                deleted_user = users.pop(user_id - 1)
                return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

# python -m uvicorn module_16_4:app
