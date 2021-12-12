class Transaction:
    def __init__(self, amount, date, description = None, merchant = None, tag = None, id = None):
        self.amount = amount
        self.date = date
        self.description = description
        self.merchant = merchant
        self.tag = tag
        self.id = id

    def update_amount(self, new_amount):
        self.amount = new_amount

    def update_date(self, new_date):
        self.date = new_date

    def update_description(self, new_description):
        self.description = new_description

    def update_merchant(self, new_merchant):
        self.merchant = new_merchant

    def update_tag(self, new_tag):
        self.tag = new_tag