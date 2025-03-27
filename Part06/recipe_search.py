# Write your solution here
def search_by_name(filename: str, word: str):
  all_recipes = []
  recipe_names = []

  with open(filename) as new_file:
    for recipe in new_file:
      recipe = recipe.strip()
      all_recipes.append(recipe)
 
  for index in range(len(all_recipes)):
    if index == 0: 
      if all_recipes[index].lower().find(word.lower()) != -1:
        recipe_names.append(all_recipes[index])

    if all_recipes[index] == "":
      if all_recipes[index + 1].lower().find(word.lower()) != -1:
        recipe_names.append(all_recipes[index + 1])
    
  return recipe_names

def search_by_time(filename: str, prep_time: int):
  all_recipes = []
  recipes_filtered = []

  with open(filename) as new_file:
    for recipe in new_file:
      recipe = recipe.strip()
      all_recipes.append(recipe)
 
  for index in range(len(all_recipes)):
    if index == 1: 
      if int(all_recipes[index]) <= prep_time:
        recipes_filtered.append(f"{all_recipes[0]}, preparation time {all_recipes[1]} min")

    if all_recipes[index] == "":
      if int(all_recipes[index + 2]) <= prep_time:
        recipes_filtered.append(f"{all_recipes[index + 1]}, preparation time {all_recipes[index + 2]} min")
  
  return recipes_filtered

def search_by_ingredient(filename: str, ingredient: str):
  all_recipes = []
  recipes_filtered = []

  with open(filename) as new_file:
    for recipe in new_file:
      recipe = recipe.strip()
      all_recipes.append(recipe)
  
  while len(all_recipes) > 0:
    start = 2
    items_in_recipes = []

    while all_recipes[start] != "":
      items_in_recipes.append(all_recipes[start])
      if start == len(all_recipes) - 1 : break
      start += 1

    if ingredient in items_in_recipes:
      recipes_filtered.append(f"{all_recipes[0]}, preparation time {all_recipes[1]} min")

    all_recipes = all_recipes[start + 1: ]
    
  return recipes_filtered

if __name__ ==  "__main__":
  found_recipes = search_by_ingredient("recipes1.txt", "milk")

  for recipe in found_recipes:
    print(recipe)
