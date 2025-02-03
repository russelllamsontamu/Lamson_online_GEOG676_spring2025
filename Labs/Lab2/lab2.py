#Part 1: Take the following list and multiply all list items together.

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

number = 1 

for i in part1:
    number = number * i 

# "i" represents the index within the loop and the word "for" creates the loop.
# This loop will run until it runs out of indexs within the loop "part1"

print ('The result of the first question after multiplying all of the numbers in the list together is:', number)

#Part 2: Take the following list and add all list items together.

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

number2 = 0 

for i in part2:
    number2 = number2 + i 
# "i" represents the index within the loop and the word "for" creates the loop.
# This loop will run until it runs out of indexs within the loop "part2"

print ('The result of the second question after adding all of the numbers in the list together is:', number2)

#Part 3: Take the following list and only add together those list items which are even.

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 

number3 = 0

for i in part3:
    if i % 2 == 0:
        number3 = number3 + i
# "i" represents the index within the loop and the word "for" creates the loop.
# This loop will run until it runs out of indexs with the loop "part3"
# The "i % 2" formula will allow us to see if the index has a remainder or not
# If there is no remainder, which is represented by " == 0", then the number in the index is even and will be used for the loop

print('The result of the third question after adding only the even numbers in the list together is:', number3)