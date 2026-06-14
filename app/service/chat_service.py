from app.ai import generate_response

def send_query(query: str) -> str:
    response = generate_response(query)
    return response