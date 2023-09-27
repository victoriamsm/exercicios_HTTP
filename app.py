from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id = UUID("c030c5e7-92ee-4b80-bdd8-ab73b5b90734"),
        first_name="Carolina",
        last_name="Bezerra",
        email="carol@email.com",
        role=[Role.role_1]
    ),
    User(
        id = UUID("4aaf4525-3c61-4f2e-9825-fbcb10691810"),
        first_name="Victória",
        last_name="Medeiros",
        email="vict@email.com",
        role=[Role.role_2]
    ),
     User(
        id = UUID("0e48bd17-b3b7-4eec-b578-4f295a26f8b9"),
        first_name="Clara",
        last_name="Martins",
        email="clara@email.com",
        role=[Role.role_3]
    )
]

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )

@app.put("/api/users/{id}")
async def put_user(id: UUID):
    db.append(id)
    return{
        "id": id

    }


