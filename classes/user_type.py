class User_type:
    def __init__(self, type_id, type_name):
        self.id = type_id
        self.type_name = type_name

    def get_type_info(self):
        return self.type_name
