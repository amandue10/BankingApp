from decimal import Decimal

from custom_exceptions.custom_exceptions import NoNegativeNumbers, NotEnoughFunds
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

    def service_deposit_into_account_by_id(self, account: Account) -> Account:
        accounts = self.service_get_all_account_information()
        updated_account = self.account_dao.deposit_into_account_by_id(account)
        deposit = Decimal(updated_account.account_balance)
        for current_account in accounts:
            current_balance = current_account.account_balance
            balance_after_deposit = current_balance + deposit
            updated_account.account_balance = balance_after_deposit
            updated_account = self.account_dao.deposit_into_account_by_id(account)
        return str(updated_account)

    def service_withdrawal_from_account_by_id(self, account: Account) -> Account:
        accounts = self.service_get_all_account_information()
        updated_account = self.account_dao.withdrawal_from_account_by_id(account)
        withdrawal = Decimal(updated_account.account_balance)
        for current_account in accounts:
            current_balance = current_account.account_balance
            balance_after_withdrawal = current_balance - withdrawal
            updated_account.account_balance = balance_after_withdrawal
            updated_account = self.account_dao.withdrawal_from_account_by_id(account)
        return str(updated_account)

    # works one way
    # def transfer_money_between_accounts_by_id(self, account: Account, account2: Account) -> Account:
    #     accounts = self.service_get_all_account_information()
    #     updated_account = self.account_dao.withdrawal_from_account_by_id(account)
    #     withdrawal = Decimal(updated_account.account_balance)
    #     for current_account in accounts:
    #         current_balance = current_account.account_balance
    #         balance_after_withdrawal = current_balance - withdrawal
    #         updated_account.account_balance = balance_after_withdrawal
    #         updated_account = self.account_dao.withdrawal_from_account_by_id(account)
    #     accounts2 = self.service_get_all_account_information()
    #     updated_account2 = self.account_dao.deposit_into_account_by_id(account2)
    #     deposit = Decimal(updated_account2.account_balance)
    #     for current_account in accounts2:
    #         current_balance = current_account.account_balance
    #         balance_after_deposit = current_balance + deposit
    #         updated_account2.account_balance = balance_after_deposit
    #         updated_account2 = self.account_dao.deposit_into_account_by_id(account2)
    #     updated_account2 = self.account_dao.transfer_money_between_accounts_by_id(account, account2)
    #     return str(updated_account2)

    # testing transfer
    # def transfer_money_between_accounts_by_id(self, account: Account, account2: Account) -> Account:
    #     accounts = self.service_get_all_account_information()
    #     updated_account = self.account_dao.withdrawal_from_account_by_id(account)
    #     updated_account2 = self.account_dao.deposit_into_account_by_id(account2)
    #     withdrawal = Decimal(updated_account.account_balance)
    #     for updated_account in accounts:
    #         current_balance = updated_account.account_balance
    #         balance_after_withdrawal = current_balance - withdrawal
    #         updated_account.account_balance = balance_after_withdrawal
    #         updated_account = self.account_dao.withdrawal_from_account_by_id(account)
    #     deposit = Decimal(updated_account.account_balance)
    #     updated_account2 = self.account_dao.deposit_into_account_by_id(account2)
    #     for updated_account2 in accounts:
    #         current_balance = updated_account2.account_balance
    #         balance_after_deposit = current_balance + deposit
    #         updated_account2.account_balance = balance_after_deposit
    #         updated_account2 = self.account_dao.transfer_money_between_accounts_by_id(account, account2)
    #     updated_account2 = self.account_dao.transfer_money_between_accounts_by_id(account, account2)
    #     return str(updated_account2)

    def service_transfer_into_bank_account(self, transfer_id: int, receive_id: int, amount):
        account = self.account_dao.get_account_by_id(transfer_id)
        if amount < -1:
            raise NoNegativeNumbers("Oops! Can't add negative funds")
        if account.account_balance < amount:
            raise NotEnoughFunds("Oops! You don't have enough funds to transfer")
        return self.account_dao.transfer_money_between_accounts_by_id(amount, transfer_id, receive_id)



