from code import interact
import time
import sys
import string
Todolist = ["."]



salute = False
_tasksTodo = ""

num = 3
integer = 1


alpthabet = string.ascii_lowercase

print("the alphabet is working and it is: ", str(alpthabet))

if input("Type Hey to start \n") == "Hey":
    print("Hey Mate! Welcome to super LISTY list")
    
else:
    print("Good Bye")
    sys.exit()

while integer < num:
    time.sleep(1)
    print("loading")
    integer = integer + 1   

if input("Do you want to Add Tasks to your List? (Y) ") == "Y":       
    print("Add Your Task HERE: ")
    _tasksTodo = input()


def func():
    outfile = open("app.txt", "a")

    outfile.write(_tasksTodo + "\n")

    outfile.close()

def storepassword():
    print("TODO")

time.sleep(0.5)
if input("Do you want to set up a Password (Y/N)") == "Y":
    print("await: yes")
else:
    print("await: no")
func()

