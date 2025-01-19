from fastapi import FastAPI
from app.controllers import image_controller

app = FastAPI()

app.include_router(image_controller.router, prefix="/api", tags=["Images"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

