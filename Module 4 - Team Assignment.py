# Edited & Modified: Jaime S.
# 10/23/2021

print("Please choose what you would like to do from the list below:")
learn_py = 1
learn_java = 2
go_swimming = 3
have_dinner = 4
bed = 5
exit = 0
print("1. Learn Python")
print("2. Learn Java")
print("3. Go swimming")
print("4. Have dinner")
print("5. Go to bed")
print("0. Exit")

command = int(input("Enter command here: "))
if command == 1:
  print("Learning Python it's a very cool programming tool to learn, but it's complicated!")
if command == 2:
  print("Java is a pretty useful programming tool to learn, but it's boring!")
if command == 3:
  print("Swimming could be fun, only if you know how to swim!")
if command == 4:
  print("Eating could be satisfying, make sure you don't eat too much")
if command == 5:
  print("Sleeping could be good for your health, but successful people don't sleep too much")
if command == 0:
  print("Exit please")

'''
Credits/References:
https://www.w3schools.com/python/python_dictionaries_loop.asp
https://www.youtube.com/watch?v=INDmGRIiyZg
'''