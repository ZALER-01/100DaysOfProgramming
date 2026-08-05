# The problem statement is:
#
# Write a program that prints the numbers from 1 to 100 (inclusive). However:
#
# If a number is divisible by 3, print "fizz" instead of the number.
# If a number is divisible by 5, print "buzz" instead of the number.
# If a number is divisible by both 3 and 5, print "fizzbuzz" instead of the number.
# Otherwise, print the number itself.


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'FizzBuzz')
    elif i % 3== 0:
        print(f'fizz')
    elif i % 5 == 0:
        print(f'Buzz')
    else:
        print(i)
