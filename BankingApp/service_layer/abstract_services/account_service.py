from abc import ABC, abstractmethod

from entities.account import Account


class AccountService(ABC):
    # create account
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    # get account information by id
    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    # update account
    @abstractmethod
    def service_update_account_information(self, account: Account) -> Account:
        pass

    # delete account
    @abstractmethod
    def service_delete_account_information(self, account_id: int) -> bool:
        pass

    # get all accounts for one customer
    @abstractmethod
    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> Account:
        pass

    # patch deposit
    @abstractmethod
    def service_deposit_into_account_by_id(self, account: Account) -> Account:
        pass
