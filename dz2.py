from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from datetime import date
import json
import os

app = FastAPI()

class User(BaseModel):
    last_name: str = Field(..., pattern=r"^[А-ЯЁ][а-яё]+$")
    first_name: str = Field(..., pattern=r"^[А-ЯЁ][а-яё]+$")
    date_of_birth: date
    phone: str = Field(..., pattern=r"^\+7\d{10}$")
    email: EmailStr

@app.post("/submit")
async def submit_user(user: User):
    data = user.dict()

    os.makedirs("data", exist_ok=True)

    file_path = f"data/{user.last_name}_{user.first_name}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=str)

    return {"message": "Данные успешно сохранены", "file": file_path}






