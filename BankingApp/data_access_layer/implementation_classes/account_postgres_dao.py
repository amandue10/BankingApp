from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDAO):
    # not working, currently working
    def create_account(self, account: Account) -> Account:
        sql = "insert into account values(default, %s, %s, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_type, account.account_name, account.account_balance))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

# working
    def get_account_by_id(self, account_id: int) -> Account:
        sql = "select * from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

# not working, needs code line 30
    def update_account_information(self, account: Account) -> Account:
        sql = "update account set balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, ())
        connection.commit()

    # currently working
    def delete_account_information(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True

    # currently working
    def get_all_account_information(self) -> list[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list
