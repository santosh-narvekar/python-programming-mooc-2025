# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):

    total_subordinates = 0
    
    if len(employee.subordinates) > 0:
        total_subordinates += len(employee.subordinates)
        
        for i in employee.subordinates:  
            total_subordinates += count_subordinates(i)

    return total_subordinates
    
    
if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)

    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))