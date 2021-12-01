from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.abstract_services.customer_service import CustomerService


class CustomerServiceImp(CustomerService):
    def __init__(self, customer_dao):
        self.customer_dao: CustomerDAOImp = customer_dao

    # create customer
    def service_create_customer_entry(self, customer: Customer) -> Customer:
        return self.customer_dao.create_customer(customer)

    # get customer information
    def service_get_customer_information(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)

    # get list of customers information
    def service_get_all_customers_information(self) -> list[Customer]:
        pass

    # update customer information
    def service_update_customer_information(self, customer: Customer) -> Customer:
        return self.customer_dao.update_customer_information(customer)

    # delete customer
    def service_delete_customer_information(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)
