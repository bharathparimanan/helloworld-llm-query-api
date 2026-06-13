from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()
app.include_router(router)

@router.get("/")
def health_check():
    return {"status": "ok"}