from typing import Optional
from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI()

def secret_header(secret: Optional[str] = Header(None)) -> None:
    print(secret)
    if not secret or secret != "SECRET":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}