# Write your solution here
def histogram(word: str):
  histogram_dict = {}

  for char in word:
    if char in histogram_dict:
      histogram_dict[char] += "*"
    else:
      histogram_dict[char] = "*"

  for key,value in histogram_dict.items():
    print(key,value)

if __name__ == "__main__":
  histogram("abba")
  histogram("statistically")