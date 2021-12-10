class Transaction:
    def __init__(self, amount, date, merchant = None, tag = None, id = None):
        self.amount = amount
        self.date = date
        self.merchant = merchant
        self.tag = tag
        self.id = id