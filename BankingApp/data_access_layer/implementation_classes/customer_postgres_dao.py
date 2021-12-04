from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities.customer import Customer
from util.database_connection import connection


class CustomerPostgresDAO(CustomerDAO):
    # working and persisting to database -pytest green
    def create_customer(self, customer: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    # pytest green
    def get_customer_information(self, customer_id: int) -> Customer:
        sql = "select * from public.customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    # working and persisting to database - pytest green
    def update_customer_information(self, customer: Customer) -> Customer:
        sql = "update customer set first_name = %s, last_name = %s where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.customer_id))
        connection.commit()
        return customer

    # working and reflecting in database - pytest green
    def delete_customer_information(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True

    # pytest green
    def get_all_customer_information(self) -> list[Customer]:
        sql = "select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customer_list = []
        for customer in customer_records:
            customer_list.append(Customer(*customer))
        return customer_list


