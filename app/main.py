from fastapi import FastAPI

from routers.greet_router import api_greet


app = FastAPI()

app.include_router(api_greet)
