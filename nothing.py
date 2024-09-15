name = input("Enter a name : ")
file = open("names.txt", "a")
file.write(name)
file.close