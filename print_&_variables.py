print("Hello world \ni am a good person")
#escape sequence character like \\n can be used to get cusrour pointer on new line


#variables
x = "red"
y = "hat"
print(x + " " + y)
    # if we want to use our variables inside the quotes than we need to use scribly braces "{}" eg:
print("{x} {y}") # red hat


#INPUT function
    #lets say wwe want an IP address so we can do nmap on that IP address

    # 1 : we can do like print("what is the IP) but we will do ->
    # Ip = input("What is the target ip ?")
    # print("the ip you entered: "+Ip)
    #but there is another way also we can =>
print("you are targeting " + input("what ip would you like to target? "))

a = 8
b = 5
c = "honey"
d = "9"
print(a + b)
# print(a + c) can not be done
# print(c + a)
print(a + int(d)) #int() converts



###TASK 1 Take a first name as a variable and last name, then print to the console "your name is : xyz name"
    #Soution:
    #print("your name is : " + input("enter your name"))

fname = input("What is your first name ?")
lname = input("What is your last name ?")
print(f"your name is {fname} {lname}")

#type function -> gives the data-type (class) of that variable
x = "dont_recon"
print(type(x))

#indexing in strings (subscripting) useful in brute forcing or word list creation
print(x[0])


#Boolean -> true and fasle