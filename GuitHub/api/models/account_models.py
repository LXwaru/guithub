from pydantic import BaseModel


class AccountIn(BaseModel):
    email: str
    username: str
    password: str


class AccountOut(BaseModel):
    id: str
    email: str
    username: str
    password: str
    

# class AccountForm(BaseModel):
#     username: str
#     password: str