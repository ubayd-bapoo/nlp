from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.get("/meta/health",
            tags=["Service Health"],
            description="This endpoint is used internally to check if the service is up")
def healthcheck():
    return Response(status_code=200)
