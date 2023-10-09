# class Employee:
#     # defining the initializer
#     def __init__(self, ID=None, salary=None, department=None):
#         self.ID = ID
#         self.salary = salary
#         self.department = department

#     def tax(self):
#         return self.salary * 0.2

#     def salaryPerDay(self):
#         return self.salary / 30


# # initializing an object of the Employee class
# Steve = Employee(3789, 2500, "Human Resources")

# # Printing properties of Steve
# print("ID =", Steve.ID)
# print("Salary", Steve.salary)
# print("Department:", Steve.department)
# print("Tax paid by Steve:", Steve.tax())
# print("Salary per day of Steve", Steve.salaryPerDay())


# class Player:
#     teamName = "Liverpool"  # class variables

#     def __init__(self, name):
#         self.name = name  # creating instance variables

#     @classmethod
#     def getTeamName(cls):
#         return cls.teamName


# obj = Player("Steve")
# obj.teamName = "Manchester United"


# print(Player.getTeamName())
# print(obj.getTeamName())
# print(obj.teamName)


class Player:
    teamName = "Liverpool"  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player("lol")
p1.demo()
Player.demo()
