from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account
from service_layer.abstract_services.account_service import AccountService


class AccountPostgresService(AccountService):
    def __init__(self, account_dao: AccountPostgresDAO):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        created_account = self.account_dao.create_account(account)
        return created_account

    def service_get_account_by_id(self, account_id: int) -> Account:
        return self.account_dao.get_account_by_id(account_id)

    def service_update_account_information(self, account: Account) -> Account:
        updated_account = self.account_dao.update_account_information(account)
        return updated_account

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)

    def service_get_all_account_information(self) -> list[Account]:
        return self.account_dao.get_all_account_information()

    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        return self.account_dao.get_all_customer_accounts_by_id(customer_id)

