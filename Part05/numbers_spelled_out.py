# Write your solution here
def  dict_of_numbers()->dict:
  ones_and_twos = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
  number_to_word = {}

  ones_index = 0
  for i in range(0,100):
    if i < 20:
      number_to_word[i] = ones_and_twos[i]
    else:
      if i % 10 == 0:
        ones_index = 0
        index = (i // 10) - 2
        number_to_word[i] = tens[index]
      else:
        ones_index += 1
        number_to_word[i] = tens[index] + "-" + ones_and_twos[ones_index]

  return number_to_word

if __name__ == "__main__":
 numbers = dict_of_numbers()
 print(numbers[2])
 print(numbers[11])
 print(numbers[45])
 print(numbers[99])
 print(numbers[0])