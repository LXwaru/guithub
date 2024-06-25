from fastapi import (
    Depends, 
    FastAPI, 
    HTTPException, 
    status
)
from routers import (
    account_routers
)


app = FastAPI()
app.include_router(account_routers.router, tags=["Accounts"])
