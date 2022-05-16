import time

list_comprehension = ["you","did"]
list_comprehension.append("it")
for concept in list_comprehension:
    print(concept)
    if (concept == list_comprehension[len(list_comprehension) - 1]):
        print("!")

# Take user input
user_input = input("How many times do you want me to say apple?")
n = int(user_input)
exit_condition = False

# Print apple, n times
while(True):
    print("apple")
    n -= 1
    
    if (n == 0):
      exit_condition = True
    
    if (exit_condition is True):
        break;

print("you have reached the end of module 0")
time.sleep(1)
print('.')
time.sleep(1)
print('..')
time.sleep(2)
print('...')
time.sleep(1)
print('....')
time.sleep(1)
print('.....')
time.sleep(5)
print('......')