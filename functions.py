import time
def myfun():
    #do this 
    print("yo")

numb = int(input("enter the number : "))
#fizbuzz with fucntions;
def fizzbuzz(num):
    if(num%15==0):
        print("fizzbuzz")
    elif(num%3==0):
        print("fizz")
    elif(num%5==0):
        print("buzz")


print("about to run the program in 5 seconds")
time.sleep(5)
fizzbuzz(numb)
