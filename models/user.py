class User:
    def __init__(self, budget, payday, id = None):
        self.budget = budget
        self.payday = payday
        self.id = id

    def update_budget(self, new_budget):
        self.budget = new_budget

    def update_payday(self, new_payday):
        self.payday = new_payday