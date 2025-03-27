# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
  station_distances = {}
  with open(filename) as new_file:
    for station in new_file:
      station = station.strip().split(";")
      if station[0] == "Longitude":
        continue
      station_distances[station[3]] = (float(station[0]),float(station[1]))

  return station_distances

def distance(stations: dict, station1: str, station2: str):
  longitude1 = stations[station1][0]
  longitude2 = stations[station2][0]
  latitude1 = stations[station1][1]
  latitude2 = stations[station2][1]
  x_km = (longitude1 - longitude2) * 55.26
  y_km = (latitude1 - latitude2) * 111.2
  distance_km = math.sqrt(x_km**2 + y_km**2)
  return distance_km

def greatest_distance(stations: dict):
  station_diff = []
  station_names = []
  max_distance = 0
  
  for station in stations:
    station_names.append(station)

  for station in station_names:
    for station_key in stations:
      distance_computed = distance(stations,station,station_key) 
      if distance_computed >= max_distance:
        max_distance = distance_computed
      station_diff.append((station, station_key, distance_computed))

  for station in station_diff:
    if station[2] == max_distance:
      return station
 
if __name__ == "__main__":
  stations = get_station_data('stations1.csv')
  station1, station2, greatest = greatest_distance(stations)
  print(station1, station2, greatest)