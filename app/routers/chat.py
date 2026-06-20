from fastapi import APIRouter, HTTPException
from app.schemas import Response, Query_Response
from app.utils import success_response, failure_response
from app.ai import  LLMClient
from app.settings import api_key, model
from app.services import generate_response

router = APIRouter()

@router.get("/query")
async def get_query(user_query:str) -> Response:
    try:
        anthropic_client = LLMClient(api_key, model)
        res_content:Response = await generate_response(anthropic_client, user_query)
        return res_content
    except RuntimeError:
        raise HTTPException(status_code=400, detail="Internal Server Error")
    finally:
        pass
