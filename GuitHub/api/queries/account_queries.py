from models.account_models import AccountIn, AccountOut

def DuplicateAccountError():
    pass 


class AccountQueries():
    def get(self, username: str) -> AccountOut:
        pass