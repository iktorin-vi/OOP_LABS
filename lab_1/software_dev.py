from lab_1.abstact_ridebike import RideBike
from lab_1.person import Person

class SoftwareDeveloper(Person, RideBike):
    def ride_bike(self):
        return f"{self} катається на велосипеді"


