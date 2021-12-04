class Account:
    def __init__(self, account_id: int, account_balance: int):
        self.account_id = account_id
        self.account_balance = account_balance

    def make_account_dictionary(self):
        return {
                "accountId": self.account_id,
                "customerId": self.customer_id,
                "accountBalance": self.account_balance
            }

    def __str__(self):
        return "account ID: {}, account balance: {}".format(self.account_id, self.account_balance)


