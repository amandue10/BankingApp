from abc import ABC, abstractmethod

from entities.customer import Customer


class CustomerService(ABC):

    # create customer method
    @abstractmethod
    def service_create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # get customer information
    @abstractmethod
    def service_get_customer_information(self, customer_id: int) -> Customer:
        pass

    # get all customer information
    @abstractmethod
    def service_get_all_customers_information(self) -> list[Customer]:
        pass

    # update customer information
    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    # delete customer information
    @abstractmethod
    def service_delete_customer_information(self, customer_id: int) -> bool:
        pass
