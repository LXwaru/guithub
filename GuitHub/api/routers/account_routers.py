from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request
)
from fastapi.security import (
    OAuth2PasswordBearer
)
from typing import Union, Annotated
from models.account_models import (
    AccountIn
)
from models.error_models import HttpError

from queries.account_queries import (
    AccountQueries,
    DuplicateAccountError
)


router = APIRouter()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/api/account/create")
async def create_account(account: AccountIn):
    return f"Hey there, {account.username}"

@router.get("/api/account")
async def get_account(username: str):
    return {"account": username}
