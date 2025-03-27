# write your solution here
def read_fruits():
  fruits_dict = {}

  with open("fruits.csv") as new_file:
    for fruit_data in new_file:
      fruit_data = fruit_data.replace("\n","")
      fruit_data = fruit_data.split(";")
      fruits_dict[fruit_data[0]] = float(fruit_data[1])
  
  return fruits_dict

if __name__ == "__main__":
  print(read_fruits())