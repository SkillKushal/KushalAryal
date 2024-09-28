import numpy as np
import time

a = np.random.rand(1000000)

b = np.random.rand(1000000)
 
 
start = time.time()
 
end = time.time()
print(f"Time taken: {end - start} seconds")

num = int(input("Enter a number : "))
total = 0
for i in str(num):
    total += int(i)
print(total)


string = input("Enter a string :  ").lower()
count = 0
count = sum[1 for char in string if char in "aeiou"]
print(count)


num = int(input("Enter a number : "))
list2 = [i**2  for i in range(1,num+1) if(i< num)]
print(list2)


for i in range(1,6):
    for j in range(1, i+1):
        print(j , end = '')

    print()   


dict1 = {}
string = input("Enter a string : ")
str2 = string.split()
m = { i: len(i) for i in str2}
print(m)    

# Counting the number of vowel letters.

# string = input("Enter a string :  ").lower()
# count = 0
# for charac in string:
#      if charac in "aeiou":
#         count += 1
# print(count)




n = 5
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end = "")
        
    print()