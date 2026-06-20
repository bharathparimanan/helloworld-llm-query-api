from app.ai import LLMClient
from app.schemas import Query_Response, Response
from app.utils import success_response

async def generate_response(client: LLMClient, query:str) -> Response:
    try:
        response:Query_Response = await client.generate_content(query)
        print(response)
        return success_response(response)
    except RuntimeError:
        raise RuntimeError(
            f"failed in midway -- service.py"
        )
    finally:
        pass