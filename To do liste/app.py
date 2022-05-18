from code import interact
import time
print("Say Hey to start the conversation!")
Todolist = ["."]


salute = False
_tasksTodo = ""

num = 3
integer = 1




saluteText = input()
if saluteText == "Hey":
    print("Hey Mate! Welcome to super LISTY list")
    salute = True


while integer < num:
    time.sleep(1)
    print("loading")
    integer = integer + 1   

if input("Do you want to Add Tasks to your List? (Y/N) ") == "Y":       
    print("Add Your Task HERE: ")
    _tasksTodo = input()


def func():
    outfile = open("app.txt", "a")

    outfile.write(_tasksTodo + "\n")

    outfile.close()


func()