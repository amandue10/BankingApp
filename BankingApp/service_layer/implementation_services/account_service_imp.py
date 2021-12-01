from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account
from service_layer.abstract_services.account_service import AccountService


class AccountServiceImp(AccountService):
    def __init__(self, account_dao: AccountDAOImp):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        return self.account_dao.create_account(account)

    def service_get_account_by_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_by_id(account_id)

    def service_update_account_information(self, account: Account) -> Account:
        return self.account_dao.update_account_information(account)

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)


