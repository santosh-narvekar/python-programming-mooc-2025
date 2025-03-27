# Write your solution here

def filter_solutions():
  correct_sol = []
  incorrect_sol = []

  with open("solutions.csv") as new_file:
    for solution in new_file:
      solution = solution.strip()
      solution = solution.split(";")
      name = solution[0]
      operation = solution[1]
      answer = int(solution[2])
    
      if "-" in operation:
        operation = operation.split("-")
        if int(operation[0]) - int(operation[1]) == answer:
          correct_sol.append(f"{name};{operation[0]}-{operation[1]};{answer}\n")
        else:
          incorrect_sol.append(f"{name};{operation[0]}-{operation[1]};{answer}\n")
      else:
        operation = operation.split("+")
        if int(operation[0]) + int(operation[1]) == answer:
          correct_sol.append(f"{name};{operation[0]}+{operation[1]};{answer}\n")
        else:
          incorrect_sol.append(f"{name};{operation[0]}+{operation[1]};{answer}\n")
  
  with open("correct.csv","w") as new_file:
    pass

  with open("incorrect.csv","w") as new_file:
    pass

  with open("correct.csv","w") as new_file:
    for sol in correct_sol:
      new_file.write(sol)

  with open("incorrect.csv","w") as new_file:
    for sol in incorrect_sol:
      new_file.write(sol)

if __name__ == "__main__":
  filter_solutions()
 