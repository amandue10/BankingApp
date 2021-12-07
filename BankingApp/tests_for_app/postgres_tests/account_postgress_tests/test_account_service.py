from custom_exceptions.custom_exceptions import NoNegativeNumbers, NotEnoughFunds
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account
from service_layer.implementation_services.account_postgres_service import AccountPostgresService

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)

account = Account(17, 1, 0)


def test_transfer_exception_negative_numbers():
    try:
        account_service.service_transfer_into_bank_account(17, 1, -100)
        assert False
    except NoNegativeNumbers as e:
        assert str(e) == "Oops! Can't add negative funds"


def test_transfer_exception_insufficient_funds():
    try:
        account_service.service_transfer_into_bank_account(17, 1, 800)
        assert False
    except NotEnoughFunds as e:
        assert str(e) == "Oops! You don't have enough funds to transfer"
