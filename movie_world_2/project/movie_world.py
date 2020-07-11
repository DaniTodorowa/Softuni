from movie_world_2.project.customer import Customer
class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15
    @staticmethod
    def customer_capacity():
        return 10
    def add_customer(customer: Customer):
        if Customer.number_of_customer < 10:
            Customer.






