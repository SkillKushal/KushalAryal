# def my_decorator(func):
#     def wrapper():
#         print("Before execution")
#         func()
#         print("After execution")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello, world!")

# say_hello()


# def validate_email(func):
#     def wrapper(user_email):
#         if useremail.endswith("@gmail.com"):
#             func(user_email)
#         else:
#             print("You're not vrit member")

#     return wrapper

#   

# get_data("akushal.177@gmail.com")











# import time
# def time_taken(func):
    
#     def wrapper(email):
#         start_time = time.time()

#         if email.endswith("@gmail.com"):
#                 time.sleep(1.5)
#                 func(email)
#         else:
#             time.sleep(1.5)
#             print("You're not vrit member")

#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(execution_time)
#     return wrapper
# @time_taken
# def get_time(email):
#     print("Accesing database")

# get_time("akushal.177@gmail.com")
        


# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return(f"({self.x},{self.y})")

#     def __add__(self,other):
#      x = self.x + other.x
#      y = self.y + other.y
#      return Point(x,y)

# p1 = Point(5,6)
# p2 = Point(6,7)
# print(p1 + p2)
    






