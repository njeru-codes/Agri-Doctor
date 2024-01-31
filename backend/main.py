from fastapi import FastAPI
from routes import login ,users

app = FastAPI()


app.include_router(login.router)
app.include_router(users.router)