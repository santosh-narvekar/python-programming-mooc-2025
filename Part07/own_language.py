# Write your solution here
import sys

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
