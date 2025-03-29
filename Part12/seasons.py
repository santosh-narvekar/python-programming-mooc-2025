# Write your solution here:
def sort_by_seasons(items: list):
  def sort_by_seasons(cur_item):
    return cur_item["seasons"]
  
  return sorted(items,key=sort_by_seasons)
