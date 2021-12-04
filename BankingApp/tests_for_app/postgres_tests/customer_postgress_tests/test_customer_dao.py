from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer

customer_dao = CustomerPostgresDAO()
customer: Customer = Customer(1, "Sam", "Denton")

random_names = {"Sam"}
random_names.add("Mary")
random_names.add("Jimmy")
random_names.add("John")
random_names.add("Henry")
random_names.add("Carey")

random_name = random_names.pop()

update_customer = Customer(1, random_name, "Denton")

delete_customer = Customer(1, "Sam", "Denton")


def test_create_player():
    created_customer = customer_dao.create_customer(customer)
    assert created_customer.customer_id != 0


def test_get_customer_success():
    returned_customer = customer_dao.get_customer_information(4)
    # assert sam_denton.first_name == "Susan" and sam_denton.last_name == "Denton"
    assert returned_customer.customer_id == 4


def test_get_all_customer_success():
    customers = customer_dao.get_all_customer_information()
    assert len(customers) > 2


def test_update_customer_success():
    updated_customer = customer_dao.update_customer_information(update_customer)
    assert updated_customer.first_name == random_name


def test_delete_customer_success():
    confirm_customer_deleted = customer_dao.delete_customer_information(3)
    assert confirm_customer_deleted


def test_get_all_customer_accounts_by_id():
    returned_customer_accounts = customer_dao.get_all_customer_accounts_by_id(5)
    assert returned_customer_accounts.customer_id == 5
    assert returned_customer_accounts.account_id == 2
    assert returned_customer_accounts.first_name == "Susanana"


