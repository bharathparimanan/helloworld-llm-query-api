from pydantic import BaseModel

class Query_Response(BaseModel):
    query: str
    model: str
    temperature: float
    answer: str
    inference_time: float
    attempts: int

class Response(BaseModel):
    status: bool
    message: str
    data: Query_Response | None