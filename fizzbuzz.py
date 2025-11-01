#FizzBuzz challenge 
# if a number is divisible by 3 , print fizz
# if a number is divisible by 5, print buzz
#if a number is divisible by both , print fizzbuzz

num = int(input("Enter the number : "))
if(num%15==0):
    print("fizzbuzz")
elif(num%3==0):
    print("fizz")
elif(num%5==0):
    print("Buzz")