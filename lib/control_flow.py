#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == 'admin' and password == '12345':
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    string = ""

    if num % 3 != 0 and num % 5 != 0:
        return num
    if num % 3 == 0:
        string += "Fizz"
    if num % 5 == 0:
        string += "Buzz"

    return string

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

# fizzbuzz() in control_flow.py returns "FizzBuzz" for num=0, num=15, num=45 F                                         [ 50%]
# fizzbuzz() in control_flow.py returns "Fizz" for num=3, num=33, num=42 F                                             [ 56%]
# fizzbuzz() in control_flow.py returns "Buzz" for num=5, num=10, num=50 F                                             [ 62%]
# fizzbuzz() in control_flow.py returns num for num=2, num=13, num=59 F                                                [ 68%]
# calculator() in control_flow.py returns sum for ("+", 1, 2), ("+", 5, 7), ("+", 9, 90) F                             [ 75%]
# calculator() in control_flow.py returns difference for ("-", 1, 2), ("-", 7, 5), ("-", 9, 9) F                       [ 81%]
# calculator() in control_flow.py returns product for ("*", 1, 2), ("*", 5, 7), ("*", 9, 10) F                         [ 87%]
# calculator() in control_flow.py returns quotient for ("/", 1, 1), ("/", 14, 7), ("/", 90, 9) F                       [ 93%]
# calculator() in control_flow.py prints "Invalid operation!" and returns None if operation invalid F                  [100%]