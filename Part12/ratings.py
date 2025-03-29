# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
  def show_rating(cur_item):
    return cur_item["rating"]
  
  return sorted(items,key=show_rating,reverse=True)
