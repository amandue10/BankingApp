from abc import ABC, abstractmethod

from entities.account import Account


class AccountDAO(ABC):

    # create account
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # get account information
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    # update account
    @abstractmethod
    def update_account_information(self, account: Account) -> Account:
        pass

    # delete account
    @abstractmethod
    def delete_account_information(self, account_id: int) -> bool:
        pass

    # get all account information List
    @abstractmethod
    def get_all_account_information(self) -> list[Account]:
        pass

    # get all accounts for one customer
    @abstractmethod
    def get_all_customer_accounts_by_id(self, customer_id: int) -> Account:
        pass
