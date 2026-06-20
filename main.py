from fastapi import FastAPI, APIRouter

app = FastAPI()

@app.get("/", tags=["root"])
def root():
    return {"message": "Hello World"}