from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": "199230",
    "username": "Gambrero",
    "email": "admin@example.com"
}

user = User(**user_data)
print(user)
print(user.email)
print(user.username)
print(user.is_active)
