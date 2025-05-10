#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self, name="Unnamed", age=0):
        self.name = name
        self.age = age

    #Instance method definition
    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
