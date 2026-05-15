##
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attirubtes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SOE"

    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")


print("Calling employee")
sam = employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
sam.travel("Jaipur")