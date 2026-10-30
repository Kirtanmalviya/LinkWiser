from fastapi import FastAPI
from .routes.userRoutes import user_routes

app = FastAPI()

app.include_router(user_routes)

@app.get("/", status_code = 200)
def health():
    return {"message": "server running"}

