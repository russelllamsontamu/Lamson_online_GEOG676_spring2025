#Part 1: Take the following list and multiply all list items together.

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

number = 1 

for i in part1:
    number = number * i 

print ('The result of the first question is:', number)

#Part 2: Take the following list and add all list items together.

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

number2 = 0 

for i in part2:
    number2 = number2 + i 

print ('The resutl of the second question is:', number2)

#Part 3: Take the following list and only add together those list items which are even.

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 

number3 = 0

for i in part3:
    if i % 2 == 0:
        number3 = number3 + i
    
print('The result of question 3 is:', number3)

