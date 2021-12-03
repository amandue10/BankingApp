from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer
from service_layer.abstract_services.customer_service import CustomerService


class CustomerPostgresService(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        created_customer = self.customer_dao.create_customer(customer)
        return created_customer

    def service_get_customer_information(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)

    def service_get_all_customers_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customer_information()

    def service_update_customer_information(self, customer: Customer) -> Customer:
        updated_customer = self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_delete_customer_information(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)


