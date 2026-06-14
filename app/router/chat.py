from fastapi import APIRouter
from app.service import send_query
router = APIRouter()

@router.get("/test")
def health_check():
    """
    function to test the server
    :return: empty JSON
    """
    return {
        "status":True,
        "message":"server running",
        "data":{}
    }

@router.get("/query")
def ask_query(query: str) -> dict:
    """
    function to query the api
    :param query: user prompt
    :return: LLM generated answer
    """
    response = send_query(query)
    return {
        "status":True,
        "message":"Ok",
        "data":{
            "query":query,
            "response":response
        }
    }
