# from wild_cat_zoo.project.caretaker import Caretaker
# from wild_cat_zoo.project.cheetah import Cheetah
# from wild_cat_zoo.project.keeper import Keeper
# from wild_cat_zoo.project.lion import Lion
# from wild_cat_zoo.project.tiger import Tiger
# from wild_cat_zoo.project.vet import Vet
#

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return f"Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [x for x in self.workers if x.name == worker_name][0]

            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_costs = sum([worker.salary for worker in self.workers])
        if self.__budget >= salary_costs:
            self.__budget -= salary_costs
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_costs = sum([animal.get_needs(self) for animal in self.animals])
        if self.__budget >= tending_costs:
            self.__budget -= tending_costs
            return f"You tended all the animals. They are happy." \
                   f" Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        lions_count = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers_count = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        chit_count = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions_count)} Lions:\n"
        result += "\n".join([str(x) for x in lions_count]) + "\n"
        result += f"----- {len(tigers_count)} Tigers:\n"
        result += "\n".join([str(x) for x in tigers_count]) + "\n"
        result += f"----- {len(chit_count)} Cheetahs:\n"
        result += "\n".join([str(x) for x in chit_count])
        return result

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        result = f"You have {len(keepers) + len(caretakers) + len(vets)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([k.__repr__() for k in keepers]) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([c.__repr__() for c in caretakers]) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join([v.__repr__() for v in vets])

        return result


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Firing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
