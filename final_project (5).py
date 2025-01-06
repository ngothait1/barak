print("**** Hello, this is my final project ****")
Name = input("what is your name? ")
print("hi " + Name +", nice to meet you")

print("************************** \nthis is a special calculator, I would neet two numbers from you")
First_number = int(input("First number: "))
second_number = int(input("second number: "))
print("thank you for putting in your numbers, " + str(First_number) + " and " + str(second_number) + "")


if First_number % 2 == 0 and second_number % 2 == 0:
    print("I can see that the First number is even\nAnd the second is even\nSo both of them are even")
elif First_number % 2 == 1 and second_number % 2 == 1:
    print("I can see that the First number is odd\nAnd the second is odd\nSo both of them are odd")
elif First_number % 2 == 0 and second_number % 2 == 1: 
     print("I can see that the First number is even\nAnd the second is odd\nSo one of them is even, and one is odd")
elif First_number % 2 == 1 and second_number % 2 == 0:
    print("I can see that the First number is odd\nAnd the second is even\nSo one of them is odd, and one is even")   


import time 
operator = input("operator (+, -, *, /) ")  

if operator == "+":
    result = First_number + second_number
    print(str(First_number) + " + " + str(second_number) + " = " + str(result)) 
elif operator == "-":
    result = First_number - second_number
    print(str(First_number) + " - " + str(second_number) + " = " + str(result))  
elif operator == "*":
    result = First_number * second_number
    print(str(First_number) + " * " + str(second_number) + " = " + str(result))   
elif operator == "/":
    if second_number != 0:
        result = First_number / second_number 
        print(str(First_number) + " / " + str(second_number) + " = " + str(result))  
    else:
        Is_Division =   input("You chose division, should the result be integer? (y/n) ") 
        print("error: num_2 is zero\nAn error had occured, please try again: ")


print("**** Thank you " + Name + " for using the calculator on " + time.ctime() + " ****")    