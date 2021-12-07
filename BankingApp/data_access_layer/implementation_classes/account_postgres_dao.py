from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDAO):
    # green pytest and persisting to database
    def create_account(self, account: Account) -> Account:
        sql = "insert into account values(default, %s, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.customer_id, account.account_balance))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    # pytest green
    def get_account_by_id(self, account_id: int) -> Account:
        sql = "select * from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

    # postman green pytest green
    def update_account_information(self, account: Account) -> Account:
        sql = "update account set customer_id = %s, account_balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (account.customer_id, account.account_balance, account.account_id))
        connection.commit()
        return account

    # pytest green, persisting to database
    def delete_account_information(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True

    # pytest green
    def get_all_account_information(self) -> list[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list

    # py test green, postman good
    def get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        sql = "select * from account where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        account_record = cursor.fetchall()
        account_list = []
        for account in account_record:
            account_list.append(Account(*account))
        return account_list

    # ------------------- Working below final 3 ----------------------------------
    # pytest green,
    # not persisting to database,
    # postman test shows business logic working
    def deposit_into_account_by_id(self, account: Account) -> Account:
        sql = "update account set account_balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (account.account_balance, account.account_id))
        connection.commit()
        return account

    # pytest green, working on service layer
    def withdrawal_from_account_by_id(self, account: Account) -> Account:
        sql = "update account set account_balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (account.account_balance, account.account_id))
        connection.commit()
        return account

    # def transfer_money_between_accounts_by_id(self, account: Account, account2: Account) -> Account:
    #     sql = "update account set account_balance = %s where account_id = %s"
    #     sql2 = "update account set account_balance = %s where account_id = %s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql,
    #                    (account.account_balance, account.account_id))
    #     cursor.execute(sql2,
    #                    (account.account_balance, account.account_id))
    #     connection.commit()
    #     return account

    def transfer_money_between_accounts_by_id(self, amount: int, transfer_id, recieve_id):
        sql = "update account set account_balance = account_balance - %s where account_id = %s"
        sql2 = "update account set account_balance = account_balance + %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (amount, transfer_id))
        cursor.execute(sql2,
                       (amount, recieve_id))
        connection.commit()
        return True
