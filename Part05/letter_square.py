# Write your solution here
characters = [
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
"Q","R","S","T","U","V","W","X","Y","Z"
]

layers = int(input("Layers: "))

run_loop = layers + (layers - 1)

center = run_loop // 2

if layers >= 2 and layers <= 26:
  for i in range(run_loop):
    for j in range(run_loop):
      if i == center and j == center:
        print(characters[0],end="")
      else:
        if abs(center - i) >= abs(center - j):
          print(characters[abs(center - i)],end="")
        else:
          print(characters[abs(center - j)],end="")
    print()