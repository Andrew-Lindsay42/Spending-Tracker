class Merchant:
    def __init__(self, name, active, icon_num = 0, id = None):
        self.name = name.capitalize()
        self.active = active
        self.icon_num = icon_num
        self.id = id

    def update_status(self, new_status):
        self.active = new_status

    def update_icon(self, new_icon):
        self.icon_num = new_icon