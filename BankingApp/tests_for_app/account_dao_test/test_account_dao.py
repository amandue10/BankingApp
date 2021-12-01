from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account

account_dao = AccountDAOImp()
test_account = Account(5, "checking", "name", 200)
updated_account = Account(4, "savings", "updated name", 250)


def test_create_account():
    created_account = account_dao.create_account(test_account)
    assert created_account.account_id != 0


def test_select_account_by_id():
    selected_account = account_dao.get_account_by_id(1)
    assert selected_account.account_id == 1


# do not need this for mvp - currently
def test_update_account_success():
    pass


def test_delete_account_success():
    result = account_dao.delete_account_information(3)
    assert result
