# TypedDict is a way in dictionary in pyhon where specify what key value should exist, dictionary should follow specific structure 
from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Harsh', 'age':'21'}

print(new_person)