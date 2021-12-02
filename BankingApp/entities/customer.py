class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, middle_name: str,
                 street: str, city: str, state: str, zip_code: str, phone: str, email: str, account_id: int):
        self.customer_id = customer_id
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def make_customer_dictionary(self):
        return {
            "customerId": self.customer_id,
            "accountId": self.account_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "middleName": self.middle_name,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zipCode": self.zip_code,
            "phone": self.phone,
            "email": self.email
        }

    def __str__(self):
        return "customer id: {}, first name: {}, last name: {}, middle name: {}," \
               "street: {}, city: {}, state: {}, zip code: {}, phone: {}," \
               "email: {}, account id: {}".format(self.customer_id, self.first_name, self.last_name, self.middle_name,
                                                  self.street,
                                                  self.city, self.state, self.zip_code, self.phone, self.email,
                                                  self.account_id)
