# Write your solution here:
def sort_by_remaining_stock(items: list):
  def order_by_stock(cur_item):
    return cur_item[2]
  
  items_by_remaining_stock = sorted(items,key=order_by_stock) 

  return items_by_remaining_stock

