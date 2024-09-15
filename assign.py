
# 1).
# def pos_arguments(*args):
#     total = 0  
#     for i in args:
#         total += i   
#     return total  

# print(pos_arguments(1, 2, 3, 4, 5))   




#2)
# def concat_strings(*args):
#     result = ''
#     for i in args:
#         result += i

#     return result

# print(concat_strings("words"," " "hello", "  "))
 

# def calculate_total_cost(**kwargs):
#     total_value = 0
#     for key,value in kwargs.items():
#         total_value += value
#         print(f"{key} = {value} ")
#     return total_value 
# print(calculate_total_cost(noodles = 75 , lays = 50 https://www.youtube.com/watch?v=3lnvkZQPfIo, chicken = 40 ))
 


# def create_student_report(name, age, **subjects_scores):
#     report = {
#         "Name": name,
#         "Age": age,
#         "Subjects": []
#     }
     
#     for subject, score in subjects_scores.items():
#         report["Subjects"].append({"Subject": subject, "Score": score})
    
#     return report

 
# report = create_student_report(
#     "Alice",
#     20,
#     Math=95,
#     Science=88,
#     English=91
# )

# print(report)

 
# list1 = ["name","age","location"]
# list2 = ["Kushal" , 18 , "Gatthaghar"]
# list3 = {a : b for a ,b in zip(list1,list2) }
# print(list3)



#Error Handling
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number : "))
# try:
#     div = num1/num2
#     print("The number is divisible")

# except ZeroDivisionError:
#     if num2 == 0:
#         print("Custom Error")

 

 

    


    
