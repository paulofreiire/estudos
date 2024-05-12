from typing import Optional
from fastapi import FastAPI, APIRouter, Depends, Header, HTTPException, status

def secret_header(secret: Optional[str] = Header(None)) -> None:
    print(secret)
    if not secret or secret != "SECRET":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

router = APIRouter(dependencies=[Depends(secret_header)])

@router.get("/route1")
async def router_route1():
    return {"route": "route1"}

@router.get("/route2")
async def router_route2():
    return {"route": "route2"}

app = FastAPI()
app.include_router(router, prefix="/router")