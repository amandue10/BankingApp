from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account


class AccountDAOImp(AccountDAO):
    # NEED TO ADD PREMADE DATA FOR TESTS WHEN THEY ARE CREATED
    account_one = Account(1, "checking", "name", 100.00)
    account_two = Account(2, "checking", "name", 200.00)
    account_three = Account(3, "checking", "name", 300.00)
    account_four = Account(4, "savings", "name", 400)
    account_list = [account_one, account_two, account_three, account_four]
    account_id_generator = 5

    # Needs to have initial balance to create
    def create_account(self, account: Account) -> Account:
        new_account = account
        new_account.team_id = AccountDAOImp.account_id_generator
        AccountDAOImp.account_id_generator += 1
        AccountDAOImp.account_list.append(new_account)
        return new_account

    def get_account_by_id(self, account_id: int) -> Account:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                return account

# update account name/info - not needed for MVP
    def update_account_information(self, account: Account) -> Account:
        pass

    def delete_account_information(self, account_id: int) -> bool:
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                index = AccountDAOImp.account_list.index(account)
                del AccountDAOImp.account_list[index]
                return True

