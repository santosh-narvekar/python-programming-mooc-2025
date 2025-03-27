# Write your solution here
def longest(strings: list) ->str:
  longest_string  = strings[0]
  for string in strings[1:]:
    if len(string) > len(longest_string):
      longest_string = string
  return longest_string

if __name__ ==  "__main__":
  if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
