# Write your solution here:
class Series:
  def __init__(self,title: str,no_of_seasons: int,genres: list):
    self.title = title
    self.no_of_seasons = no_of_seasons
    self.genres = genres
    self.rating = 0
    self.no_of_ratings = 0

  def rate(self,rating: int):
    self.no_of_ratings += 1
    self.rating += rating

  def __str__(self):
    genres = ", ".join(self.genres)
    rating_template = "no ratings"
    if self.no_of_ratings > 0:
      average = round(self.rating / self.no_of_ratings,1)
      rating_template = f"{self.no_of_ratings} ratings, average {average} points"

    return f"{self.title} ({self.no_of_seasons} seasons)\ngenres: {genres}\n{rating_template}"

def minimum_grade(rating: float,series_list: list) -> list:
  filtered_series = []
  for series in series_list:
    if series.rating >= rating:
      filtered_series.append(series)
  return filtered_series

def includes_genre(genre: str, series_list: list) -> list:
  filtered_series = []
  for series in series_list:
    if series.genres.count(genre) != 0:
      filtered_series.append(series)
  return filtered_series

if __name__ == "__main__":
  s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
  s1.rate(5)

  s2 = Series("South Park", 24, ["Animation", "Comedy"])
  s2.rate(3)

  s3 = Series("Friends", 10, ["Romance", "Comedy"])
  s3.rate(2)

  series_list = [s1, s2, s3]

  print("a minimum grade of 4.5:")
  for series in minimum_grade(4.5, series_list):
    print(series.title)

  print("genre Comedy:")
  for series in includes_genre("Comedy", series_list):
    print(series.title)