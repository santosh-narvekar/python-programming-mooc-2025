# Write your solution here
def search(products: list, criterion: callable) -> list:
  filtered_products = []
  for product in products:
    if criterion(product):
      filtered_products.append(product)
  
  return filtered_products

