from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def get_response():
    return "serving chat"

