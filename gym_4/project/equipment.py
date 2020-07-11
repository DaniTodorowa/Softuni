class Equipment:
    autoincrenemtal_id = 1
    def __init__(self, name):
        self.name = name
        self.id = Equipment.autoincrenemtal_id
        Equipment.autoincrenemtal_id += 1
    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_netx_id():
        return Equipment.autoincrenemtal_id


