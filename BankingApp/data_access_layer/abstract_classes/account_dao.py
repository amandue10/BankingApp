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
