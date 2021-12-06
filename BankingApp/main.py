from flask import Flask, request, jsonify
from unicodedata import decimal

from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.account import Account
from entities.customer import Customer
from service_layer.abstract_services import account_service
from service_layer.implementation_services.account_postgres_service import AccountPostgresService
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresService

# import logging
#
# logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")
app: Flask = Flask(__name__)

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)
account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)


# create player method - Postman Test not working
@app.post("/customer")
def create_customer_entry():
    # try:
    customer_data = request.get_json()
    new_customer = Customer(
        customer_data["customerId"],
        customer_data["firstName"],
        customer_data["lastName"]
    )
    customer_to_return = customer_service.service_create_customer_entry(new_customer)
    customer_as_dictionary = customer_to_return.make_customer_dictionary()
    customer_as_json = jsonify(customer_as_dictionary)
    return customer_as_json


# get customer personal information - Postman Test Working
@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    result = customer_service.service_get_customer_information(int(customer_id))
    result_as_dictionary = result.make_customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


# postman test working
@app.get("/customer")
def get_all_customers_information():
    customers_as_customers = customer_service.service_get_all_customers_information()
    customers_as_dictionary = []
    for customers in customers_as_customers:
        dictionary_customer = customers.make_customer_dictionary()
        customers_as_dictionary.append(dictionary_customer)
    return jsonify(customers_as_dictionary)


# update customer - Postman Test not working
@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    # try:
    customer_data = request.get_json()
    new_customer = Customer(
        int(customer_id),
        customer_data["firstName"],
        customer_data["lastName"]

    )
    updated_customer = customer_service.service_update_customer_information(new_customer)
    return "Customer updated successfully, the customer info is now " + str(updated_customer)


# delete customer information - Postman Test Working
@app.delete("/customer/<customer_id>")
def delete_customer_information(customer_id: str):
    result = customer_service.service_delete_customer_information(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(customer_id)


# create - postman working
@app.post("/account")
def create_account():
    # try:
    body = request.get_json()
    new_account = Account(
        body["accountId"],
        body["customerId"],
        body["accountBalance"]
    )
    account_to_return = account_service.service_create_account(new_account)
    account_as_dictionary = account_to_return.make_account_dictionary()
    account_as_json = jsonify(account_as_dictionary)
    return account_as_json


# postman test working
@app.get("/account/<account_id>")
def get_account_by_id(account_id: str):
    result = account_service.service_get_account_by_id(int(account_id))
    result_as_dictionary = result.make_account_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


# postman test working
@app.get("/account")
def get_all_accounts():
    accounts = account_service.service_get_all_account_information()
    accounts_as_dictionaries = []
    for account in accounts:
        dictionary_account = account.make_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200


# postman test working
@app.get("/accounts/<customer_id>")
def get_all_customer_accounts_by_id(customer_id: str):
    results = account_service.service_get_all_customer_accounts_by_id(int(customer_id))
    customer_accounts_as_dictionaries = []
    for account in results:
        customer_accounts_dictionaries = account.make_account_dictionary()
        customer_accounts_as_dictionaries.append(customer_accounts_dictionaries)
    return jsonify(customer_accounts_as_dictionaries), 200


# post man working
@app.patch("/account/<account_id>")
def update_account(account_id: str):
    account_data = request.get_json()
    new_account = Account(
        int(account_id),
        account_data["customerId"],
        account_data["accountBalance"]

    )
    updated_account = account_service.service_update_account_information(new_account)
    return "Account updated successfully, the Account info is now " + str(updated_account)


# postman test working
@app.delete("/account/<account_id>")
def delete_account(account_id: str):
    result = account_service.service_delete_account_information(int(account_id))
    if result:
        return "Account with id {} was deleted successfully".format(account_id)
    else:
        return "Something went wrong: account with id {} was not deleted".format(account_id)


# post works as intended, not persisting to database
@app.patch("/deposit/<account_id>")
def deposit_account(account_id):
    account_data = request.get_json()
    dep_account = Account(
        account_data["accountId"],
        account_data["customerId"],
        account_data["accountBalance"]
    )
    updated_account = account_service.service_deposit_into_account_by_id(dep_account)
    return updated_account


# patch works as intended, not persisting to database
@app.patch("/withdrawal/<account_id>")
def withdrawal_account(account_id):
    account_data = request.get_json()
    dep_account = Account(
        account_data["accountId"],
        account_data["customerId"],
        account_data["accountBalance"]
    )
    updated_account = account_service.service_withdrawal_from_account_by_id(dep_account)
    return updated_account


# testing
# @app.patch("/transfer/<account_id>/<account_id>")
# def transfer_account(account_id):
#     account_data = request.get_json()
#     tran_account = Account(
#         account_data["accountId"],
#         account_data["customerId"],
#         account_data["accountBalance"]
#     )
#     transfer = account_service.transfer_money_between_accounts_by_id(tran_account)
#     return transfer


app.run()
