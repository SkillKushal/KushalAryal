"""  Q1  Write a Program to Define a Function describe_pet that accepts a variable number of keyword arguments (**kwargs).
 
The function should print the details of these keyword arguments as "property: value". Call this function with pet details like name, age, and type."""
def describe_pet(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

     
describe_pet(name = "Tommy", age = 10, type = "husky")



 


""" Q2 Standard Deviation   """
import math
num_list = [6,14,25,37,46,57,63,78,83,94]
mean = sum(num_list)/len(num_list)
sq_list = [(num - mean)**2   for num in num_list]
std = sum(sq_list)/len(num_list)
stdev = math.sqrt(std)
print(stdev)





"""  
1. **Personal Information**
   - Create a variable `name` (str) to store the user's name.
   - Create a variable `age` (int) to store the user's age.
   - Print a greeting message using these variables, e.g., `"Hello, my name is Alice and I am 30 years old."` """

name = input("Enter the user's name : ")
age = int(input("Enter your age "))
print(f"Hello, My name is {name} and I am {age} years old.")







fav_hobbies = ["Singing", "Coding", "Playing"]
print(fav_hobbies)
fav_hobbies.append("Dancing")
print(fav_hobbies)



"""3. **Screen Dimensions**
   - Define a tuple `screen_dimensions` with two integers representing the width and height of the user's preferred screen size for the app.
   - Attempt to modify one of the values in the tuple to simulate an attempt to change screen preferences and comment on the outcome."""

screen_dimensions = [25,65]
try:
    screen_dimensions[1]= 400
    

except TypeError:
    print("You cannot modify tuple. ")
else:
    print(screen_dimensions)



"""  **Pet Description**
   - Create a dictionary `pet` to describe the user's pet. It should include keys for `type`, `name`, `age`, and later, `color`.
   - Add a `color` key to the `pet` dictionary with an appropriate value and print the pet's name and color.  """
 
pet = {"type" :"Husky", "name":"Tommy" , "age" : 5  }
pet["color"] = "Orange"
print(pet)




 
""" **Adult Status**
   - Determine if the user is an adult with a boolean variable `is_adult`. Consider someone an adult if they are 18 years old or more.
   - Using conditional logic, print `"I am an adult."` if true, and `"I am not an adult."` if false.
  """
age = int(input("Enter your age: "))
if age >= 18:
   is_adult = True
else:
    is_adult = False


if is_adult:
    print("You're an adult")
else:
    print("You're not an adult")




books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1951, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]

""" Create a Book Filtering Function

Given the list books as shown below, write a Python function named `filter_books` that filters books based on *genre* and *publication year*. The function should take two parameters: `genre (a string)` and `year (an integer)`. It should return a list of book titles that match the given genre and have been **published on or after** the specified year.

- Example usage : `print(filter_books("Fiction", 1980))`
- Expected output: `['The Alchemist', 'The Catcher in the Rye']`"""
 
def filter_book(_genre, _year):
    list3 = [name for name, genre, year, amount in books if genre == _genre and year >= _year]
    return list3

list4 = filter_book("Fiction",1920)
print(list4)


""" **Task 02** : Write a Python function named `borrowing_stats` that uses dictionary comprehension to create and return a dictionary. This dictionary should map each book's title to the number of times it has been borrowed, but only include books from the "`Fiction`" genre.


- Example usage : `print(borrowing_stats(books))`
- Expected output: `{'The Alchemist': 250, 'Pride and Prejudice': 200, 'To Kill a Mockingbird': 180, 'The Catcher in the Rye': 220, '1984': 190}`   """
 
def burrowing_stats():
    
    dict3 = {name: amount for name, genre, year, amount in books if genre == "Fiction"}
    print(dict3)

burrowing_stats()
  

""" ### Question: File Read and Write
**Write a Program that Uses Functions `write_to_file` and `read_from_file`**:
- `write_to_file(filename, content)`: Writes `content` to a file named `filename`. If the file doesn't exist, it should be created.
- `read_from_file(filename)`: Reads and prints the content of a file named `filename`.
Call `write_to_file` to write "Hello, Python!" to a file named "greetings.txt", then call `read_from_file` to read and print the content of this file. """

 
with open(filename, "a") as file:
        file.write(content)
def read_from_file(filename):
     with open(filename, "r") as file:  
            content = file.read()       
            print(content)

write_to_file("greetings.txt", "Hello,Python!") 
read_from_file("greetings.txt") 



#OOP
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, rental_price):
        self.__vehicle_id = vehicle_id
        self.__brand = brand
        self.__rental_price = rental_price

    
    def get_brand(self):
        return self.__brand

    def get_id(self):
        return self.__vehicle_id

    def get_price(self):
        return self.__rental_price
 
    def total_rental_cost(self, rental_days):
        return self.__rental_price * rental_days

   
    @abstractmethod
    def display_details(self):
        pass

 
class Car(Vehicle):
    def __init__(self, brand, vehicle_id, rental_price, number_of_doors):
        super().__init__(vehicle_id, brand, rental_price)
        self.__number_of_doors = number_of_doors

    
    def get_number_of_doors(self):
        return self.__number_of_doors

    def set_number_of_doors(self, number_of_doors):
        self.__number_of_doors = number_of_doors
 
    def display_details(self):
        print(f"Brand of vehicle is {self.get_brand()}")
        print(f"Vehicle ID is {self.get_id()}")
        print(f"Rental price per day is ${self.get_price()}")
        print(f"Number of doors is {self.get_number_of_doors()}")
 
if __name__ == "__main__":
    car = Car("Mercedes", "DEF123", 100, 4)
 
    car.display_details()
 
    total_rent = car.total_rental_cost(10)
    print(f"Total rent for 10 days is ${total_rent}")









       