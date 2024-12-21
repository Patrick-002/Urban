from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def user_registration(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example= 'UrbanUser')]
                    , age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example= '24')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def user_update(user_id: str, username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example= 'UrbanUser')]
                    , age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example= '24')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"The user {user_id} is deleted"

# python -m uvicorn module_16_3:app
