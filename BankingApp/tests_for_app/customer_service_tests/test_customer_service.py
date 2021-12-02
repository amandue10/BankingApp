from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.implementation_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
customer = Customer(4, "Sam", "Denton", "C", "400 Dawson Drive", "Edinburg",
                    "Texas", "80247", "956-250-7894", "tom@gmail.com", 2)


# create customer test
# def test_validate_create_customer_entry(self, customer: Customer) -> Customer:
#     pass


# get customer information
# def test_validate_get_customer_information(self, customer_id: int) -> Customer:
#     return self.customer_dao.get_customer_information(customer_id)


# get list of customers information
# def test_validate_get_all_customers_information(self) -> list[Customer]:
#     pass


# update customer information
# def test_validate_update_customer_information(self, customer: Customer) -> Customer:
#     pass


# delete customer
# def test_validate_delete_customer_information(self, customer_id: int) -> bool:
#     pass
