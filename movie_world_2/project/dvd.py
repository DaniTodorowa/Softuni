class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def is_rent(a):
        if a:
            return "rented"
        return "not rented"

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {self.is_rent()}"

    @classmethod
      def from_date(cls, id: int, name: str, date: str, age_restriction: int):
       my_dict_monts = {1:"January", 2:"February",3:"March",4:"April",5:"May",6:"June",7:"July"





