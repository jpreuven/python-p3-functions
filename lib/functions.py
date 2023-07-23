#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    print(type(number))
    if (type(number) != int and type(number) != float):
        # print("hello")
        return None
    else:
        print(number/2)
        return number/2

halve(99)