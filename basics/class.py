# class Employee:
#     # defining the properties and assigning them None
#     ID: int | None = None
#     salary: int | None = None
#     department: str | None = None


# # cerating an object of the Employee class
# Steve = Employee()

# # assigning values to properties of Steve - an object of the Employee class
# Steve.ID = 3789
# Steve.salary = 2500
# Steve.department = "Human Resources"
# # Steve.title = "Manager"

# # Printing properties of Steve
# print("ID =", Steve.ID)
# print("Salary", Steve.salary)
# print("Department:", Steve.department)


# class Employee:
#     def __init__(self, ID, salary, department):
#         self.ID = ID
#         self.salary = salary
#         self.department = department


# # creating an object of the Employee class with default parameters
# Steve = Employee(3789, 2500, "Human Resources")

# # Printing properties of Steve
# print("ID :", Steve.ID)
# print("Salary :", Steve.salary)
# print("Department :", Steve.department)


# class Player:
#     teamName = "Liverpool"  # class variables

#     def __init__(self, name):
#         self.name = name  # creating instance variables


# p1 = Player("Mark")
# p2 = Player("Steve")

# Player.teamName = "Manchester United"

# print("Name:", p1.name)
# print("Team Name:", p1.teamName)
# print("Name:", p2.name)
# print("Team Name:", p2.teamName)


class Player:
    teamName = "Liverpool"  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []


p1 = Player("Mark")
p1.formerTeams.append("Barcelona")
p2 = Player("Steve")
p2.formerTeams.append("Chelsea")

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)
