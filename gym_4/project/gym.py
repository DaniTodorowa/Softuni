class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self,trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    def add_equipment(self, equipment):
        if equipment  not in self.equipment:
            self.equipment.append(equipment)
    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self,subscription_id):
        subscription = [s for s in self.subscriptions if s.id ==subscription_id][0]
        result = subscription.__repr__()



# from gym_4.project.equipment import Equipment
# from gym_4.project.customer import Customer
# from gym_4.project.exercise_plan import ExercisePlan
# from gym_4.project.trainer import Trainer
# from gym_4.project.subscription import Subscription

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))










