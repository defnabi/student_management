students = []

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Students")


    choice = input("Choice:")

    if choice == "1" :
        name = input ("Name: ")
        students.append(name)

    elif choice == "2":
        print(students)
        
