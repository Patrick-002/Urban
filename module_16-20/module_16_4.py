from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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
async def user_registration(username: str, age: str) -> User:
    new_user = User(id=len(users) + 1, username=username, age=age)
    new_user.id = len(users) + 1
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def user_update(user_id: str, username: str, age: str) -> User:
    try:
        edit_user = users[int(user_id) - 1]
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
