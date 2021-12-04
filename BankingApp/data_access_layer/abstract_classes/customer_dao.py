from abc import ABC, abstractmethod

from entities.customer import Customer


class CustomerDAO(ABC):

    # create player method
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # get customer information
    @abstractmethod
    def get_customer_information(self, customer_id: int) -> Customer:
        pass

    # update customer information
    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    # delete customer information
    @abstractmethod
    def delete_customer_information(self, customer_id: int) -> bool:
        pass

    # get all customer information List
    @abstractmethod
    def get_all_customer_information(self) -> list[Customer]:
        pass


