"""  Q1  Write a Program to Define a Function describe_pet that accepts a variable number of keyword arguments (**kwargs).
 
The function should print the details of these keyword arguments as "property: value". Call this function with pet details like name, age, and type."""



 


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




  

# fav_hobbies = ["Singing", "Coding", "Playing"]
# print(fav_hobbies)
# fav_hobbies.append("Dancing")
# print(fav_hobbies)


 

# screen_dimensions = [25,65]
# try:
#     screen_dimensions[1]= 400
    

# except TypeError:
#     print("You cannot modify tuple. ")
# else:
#     print(screen_dimensions)



 
# pet = {"type" :"Husky", "name":"Tommy" , "age" : 5  }
# pet["color"] = "Orange"
# print(pet)




 

# age = int(input("Enter your age: "))
# if age >= 18:
#    is_adult = True
# else:
#     is_adult = False


# if is_adult:
#     print("You're an adult")
# else:
#     print("You're not an adult")




# books = [
#     ("The Alchemist", "Fiction", 1988, 250),
#     ("The Da Vinci Code", "Mystery", 2003, 300),
#     ("A Brief History of Time", "Science", 1988, 150),
#     ("The Theory of Everything", "Science", 2002, 100),
#     ("Pride and Prejudice", "Fiction", 1813, 200),
#     ("To Kill a Mockingbird", "Fiction", 1960, 180),
#     ("The Catcher in the Rye", "Fiction", 1951, 220),
#     ("Angels & Demons", "Mystery", 2000, 210),
#     ("The Grand Design", "Science", 2010, 90),
#     ("1984", "Fiction", 1949, 190)
# ]


 
# def filter_book(_genre, _year):
#     list3 = [name for name, genre, year, amount in books if genre == _genre and year >= _year]
#     return list3

# list4 = filter_book("Fiction",1920)
# print(list4)



 
# def burrowing_stats():
    
#     dict3 = {name: amount for name, genre, year, amount in books if genre == "Fiction"}
#     print(dict3)

# burrowing_stats()
  



 
#     with open(filename, "a") as file:
#         file.write(content)
# def read_from_file(filename):
#      with open(filename, "r") as file:  
#             content = file.read()       
#             print(content)

# write_to_file("greetings.txt", "Hello,Python!") 
# read_from_file("greetings.txt") 



#OOP
# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     def __init__(self, vehicle_id, brand, rental_price):
#         self.__vehicle_id = vehicle_id
#         self.__brand = brand
#         self.__rental_price = rental_price

    
#     def get_brand(self):
#         return self.__brand

#     def get_id(self):
#         return self.__vehicle_id

#     def get_price(self):
#         return self.__rental_price
 
#     def total_rental_cost(self, rental_days):
#         return self.__rental_price * rental_days

   
#     @abstractmethod
#     def display_details(self):
#         pass

 
# class Car(Vehicle):
#     def __init__(self, brand, vehicle_id, rental_price, number_of_doors):
#         super().__init__(vehicle_id, brand, rental_price)
#         self.__number_of_doors = number_of_doors

    
#     def get_number_of_doors(self):
#         return self.__number_of_doors

#     def set_number_of_doors(self, number_of_doors):
#         self.__number_of_doors = number_of_doors
 
#     def display_details(self):
#         print(f"Brand of vehicle is {self.get_brand()}")
#         print(f"Vehicle ID is {self.get_id()}")
#         print(f"Rental price per day is ${self.get_price()}")
#         print(f"Number of doors is {self.get_number_of_doors()}")
 
# if __name__ == "__main__":
#     car = Car("Mercedes", "DEF123", 100, 4)
 
#     car.display_details()
 
#     total_rent = car.total_rental_cost(10)
#     print(f"Total rent for 10 days is ${total_rent}")









       