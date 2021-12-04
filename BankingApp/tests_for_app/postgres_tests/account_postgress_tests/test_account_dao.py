from email.policy import default

from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account

account_dao = AccountPostgresDAO()

new_account = Account(1, "checking", "new", 200.00)
update_account = Account(1, "checking", "new", 200.00)
delete_account = Account(1, "checking", "new", 200.00)
new_balance = Account(1, "checking", "new", 200.00)


def test_create_account_success():
    account_result = account_dao.create_account(new_account)
    assert account_result.account_id != 0


def test_select_account_by_id_success():
    initial_account = account_dao.get_account_by_id(1)
    assert initial_account.account_id == 1


def test_select_all_account_success():
    accounts = account_dao.get_all_account_information()
    assert len(accounts) >= 2


def test_update_account_success():
    updated_account = account_dao.update_account_information(update_account)
    assert updated_account.account_balance == new_balance


def test_delete_account_success():
    confirm_account_deleted = account_dao.delete_account_information(3)
    assert confirm_account_deleted


