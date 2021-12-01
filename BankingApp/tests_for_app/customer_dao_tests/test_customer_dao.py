from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer

customer_dao_imp = CustomerDAOImp()
customer = Customer(4, "Sam", "Denton", "C", "400 Dawson Drive", "Edinburg",
                    "Texas", "80247", "956-250-7894", "tom@gmail.com")
test_customer = Customer(4, "Sam", "Denton", "C", "400 Dawson Drive", "Edinburg",
                         "Texas", "80247", "956-250-7894", "tom@gmail.com")


def test_create_customer_success():
    new_customer: Customer = customer_dao_imp.create_customer(test_customer)
    print(new_customer.customer_id)
    assert new_customer.customer_id != 0


def test_select_customer_by_id_success():
    returned_customer: Customer = customer_dao_imp.get_customer_information(1)
    assert returned_customer.customer_id == 1


# def test_select_all_customers_success():
#     customer = customer_dao.get_all_customer_information()
#     assert len(customer) >= 2

def test_update_customer_success():
    updated_customer = Customer(5, "Sam", "Houston", "C", "400 Dawson Drive", "Edinburg",
                                "Texas", "80245", "956-250-7894", "tom@gmails.com")
    updated_customer1: Customer = customer_dao_imp.update_customer_information(updated_customer)
    assert updated_customer.zip_code == "80245"


def test_delete_customer_success():
    confirm_customer_deleted = customer_dao_imp.delete_customer_information(3)
    assert confirm_customer_deleted
