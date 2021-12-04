from email.policy import default

from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account

account_dao = AccountPostgresDAO()

new_account = Account(1, 1, 200.00)
update_account = Account(1, 1, 210.00)
delete_account = Account(2, 1, 200.00)
new_balance = Account(1, 1, 1200.00)
new_balances = 210.00


def test_create_account_success():
    account_result = account_dao.create_account(new_account)
    assert account_result.account_id != 0


def test_select_account_by_id_success():
    initial_account = account_dao.get_account_by_id(4)
    assert initial_account.account_id == 4


def test_select_all_account_success():
    accounts = account_dao.get_all_account_information()
    assert len(accounts) >= 2


def test_update_account_success():
    updated_account = account_dao.update_account_information(update_account)
    assert updated_account.account_balance == new_balances


def test_delete_account_success():
    confirm_account_deleted = account_dao.delete_account_information(3)
    assert confirm_account_deleted


# needs configuration
def test_get_all_customer_accounts_by_id():
    returned_customer_accounts = account_dao.get_all_customer_accounts_by_id(5)
    # assert returned_customer_accounts.customer_id == 5
    # assert returned_customer_accounts.account_id == 4
    # assert returned_customer_accounts.account_balance == 300.00
    assert len(returned_customer_accounts) >= 3
