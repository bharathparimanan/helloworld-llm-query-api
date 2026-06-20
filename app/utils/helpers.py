from app.schemas import Response

def success_response(data) -> Response:
    return Response(
        data=data,
        status=True,
        message="success"
    )

def failure_response(data) -> Response:
    return Response(
        data=data,
        status=False,
        message="failure"
    )