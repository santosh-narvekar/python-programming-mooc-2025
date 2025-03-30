# Write your solution here
import sys
# APPROACH 1
def check(cur_value,values_found):
  try:
    cur_value = int(cur_value)
  except:
    if cur_value in values_found:
      cur_value = values_found[cur_value]
    else:
      cur_value = 0
  return cur_value

def print_val(var,generated_values,values):
  var = check(var,values)
  generated_values.append(var)

def commands(command,var,val,values):
  val = check(val,values)
  if command == "MOV": values[var] = val
  if var not in values:
    values[var] = 0
  if command == "ADD": values[var] += val
  if command == "SUB": values[var] -= val
  if command == "MUL": values[var] *= val

def jump_via_location(location,program_commands):
  return program_commands.index(location+":")

def jump_via_condition(oph1,opr,oph2,location,program_commands,values):
  oph1 = check(oph1,values)
  oph2 = check(oph2,values)
  
  operations = {
    ">": oph1 > oph2,
    "<": oph1 < oph2,
    ">=": oph1 >= oph2,
    "<=": oph1 <= oph2,
    "==": oph1 == oph2,
    "!=": oph1 != oph2
  }

  if operations[opr]:
    return program_commands.index(location+":")
  else:
    return -1
  
def run(program_commands: list):
  generated_values = []
  values = {}
  count = 0
  def run_loop(program_commands_in_loop,count,program_commands = program_commands):
    sys.setrecursionlimit(10000)

    for command in program_commands_in_loop:
      command = command.split(" ")
      instruction = command[0]
      
      if instruction == "END":
        return generated_values

      if instruction in ["MOV","ADD","SUB","MUL"]:
       var = command[1]
       val = command[2]
       commands(instruction,var,val,values)

      if instruction == "PRINT":
        var = command[1]
        print_val(var,generated_values,values)

      if instruction == "IF":
        oph1 = command[1]
        opr = command[2]
        oph2 = command[3]
        location = command[-1]
        index = jump_via_condition(oph1,opr,oph2,location,program_commands,values)
        if index != -1:
          run_loop(program_commands[index:],count)
          break

      if instruction == "JUMP":
        location = command[1]
        index = jump_via_location(location,program_commands)
        run_loop(program_commands[index:],count)
        break
    count += 1

    if count >= 9097:
      return
    
  run_loop(program_commands,count,program_commands)
  
  return generated_values

# APPROACH 2

def determine_value(value: int,variables: dict) -> int:
  if value in variables:
    return int(variables[value])
  
  return int(value)

def initialize_variables(variables: dict) -> None:
  all_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  for letter in all_letters:
    variables[letter] = 0

def run(program: list) -> list:
  print_list = []
  variables = {}
  locations = []
  initialize_variables(variables)

  for position,instruction in enumerate(program):
    if ":" in instruction:
      location = instruction[:-1]
      locations.append((location,position))
  
  i = 0

  while i < len(program):
    instruction = program[i]
    parts = instruction.split(" ")
    command = parts[0]
    
    if command == "PRINT":
      value = parts[1]
      value = determine_value(value,variables)
      print_list.append(value)

    if command == "MOV" :
      var = parts[1]
      value = parts[2]
     
      value = determine_value(value,variables)
      variables[var] = value

    if command == "ADD":
      var = parts[1]
      value = parts[2]

      value = determine_value(value,variables)
      variables[var] += value
    
    if command == "SUB":
      var = parts[1]
      value = parts[2]

      value = determine_value(value,variables)
      variables[var] -= value
    
    if command == "MUL":
      var = parts[1]
      value = parts[2]

      value = determine_value(value,variables)
      variables[var] *= value

    if command == "JUMP":
      to_jump = parts[1]
      for loc in locations:
        if loc[0] == to_jump:
          i = loc[1]

    if command == "IF":
      oph1 = parts[1]
      opr = parts[2]
      oph2 = parts[3]

      oph1 = determine_value(oph1, variables)
      oph2 = determine_value(oph2, variables)
      jump_location = parts[5]
      if eval(f"{oph1} {opr} {oph2}"):
        for loc in locations:
          if loc[0] == jump_location:
            i = loc[1]
      
    i += 1

  return print_list

