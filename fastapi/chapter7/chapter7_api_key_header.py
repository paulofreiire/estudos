from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.params import Depends
from fastapi.security import APIKeyHeader
API_TOKEN = "SECRET"

app = FastAPI()

api_key_header = APIKeyHeader(name="Token")

async def api_token(token: str =
Depends(APIKeyHeader(name="Token"))):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

@app.get("/protected-route", dependencies=[Depends(api_token)])
async def protected_route():
    return {"hello": "world"}