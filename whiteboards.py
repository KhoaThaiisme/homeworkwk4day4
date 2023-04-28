#Write a function that prints the numbers from 1 to n. But for multiples of 3, print ‘Fizz’ instead of the number, and for multiples of 5, print ‘Buzz’. For numbers that are multiples of both 3 and 5, print ‘FizzBuzz’
# Sample output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11

def fizzBuzz(num): 
    for n in range(1, num+1):
        if n % 5 ==0 and n % 3 == 0:
           print('FizzBuzz') 
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0:
            print('Fizz')
        else:
            print(n)

print(fizzBuzz(20))