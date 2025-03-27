# Write your solution here

no_of_students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))
groups_formed = no_of_students / desired_group_size 

groups_forming = no_of_students // desired_group_size

if (  no_of_students % desired_group_size == 0 ):
    print(f"Number of groups formed: {groups_forming}")
else:
    print(f"Number of groups formed: {groups_forming + 1}")