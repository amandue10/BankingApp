class Account:
    def __init__(self, account_id: int, account_type: str, account_name: str, account_balance: int):
        self.account_id = account_id
        self.account_type = account_type
        self.account_name = account_name
        self.account_balance = account_balance

    def make_account_dictionary(self):
        return {
                "accountId": self.account_id,
                "accountType": self.account_type,
                "accountName": self.account_name,
                "accountBalance": self.account_balance
            }

    def __str__(self):
        return "account ID: {}, account type: {}, account name: {}, account balance: {}".format(self.account_id,
                 self.account_type, self.account_name, self.account_balance)


