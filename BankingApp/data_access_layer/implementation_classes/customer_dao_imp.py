from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities import customer
from entities.customer import Customer


class CustomerDAOImp(CustomerDAO):
    # premade customers to test methods
    premade_customer = Customer(1, "Amanda", "Gonzalez", "Christine", "900 Dawson Dr",
                                "Denver", "Colorado", "80247", "956-255-5655", "email@aol.com", 1)
    premade_customer_two = Customer(2, "Amanda", "Gonzalez", "Christine", "900 Dawson Dr",
                                    "Denver", "Colorado", "80247", "956-255-5655", "email@yahoo.com", 2)
    # customer created to be deleted
    to_delete = Customer(3, "Amanda", "Gonzalez", "Christine", "900 Dawson Dr",
                         "Denver", "Colorado", "80247", "956-255-5655", "email@gmail.com", 3)

    # creating a list to use as a "database"
    customer_list = [premade_customer, premade_customer_two, to_delete]
    # assign customer id's unique
    customer_id_generator = 7

    def get_customer_information(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def update_customer_information(self, customer: Customer) -> Customer:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                CustomerDAOImp.customer_list[index] = customer
                return customer

    def delete_customer_information(self, customer_id: int) -> bool:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                del CustomerDAOImp.customer_list[index]
                return True

    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_id_generator += 1
        CustomerDAOImp.customer_list.append(customer)
        return customer

    def get_all_customer_information(self) -> list[Customer]:
        return CustomerDAOImp.customer_list
