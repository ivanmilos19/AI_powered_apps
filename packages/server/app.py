import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from routes import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(router)

register_tortoise(
    app,
    db_url=os.getenv("DATABASE_URL"),
    modules={"models": ["database.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
