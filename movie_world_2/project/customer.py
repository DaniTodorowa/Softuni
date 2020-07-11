class Customer:
    number_of_customer = 0
    def __init__(self,name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []
        Customer.number_of_customer +=1
    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([str(x)for x in self.rented_dvds])})"