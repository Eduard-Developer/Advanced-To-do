from code import interact
import time
import sys
import string
Todolist = ["."]



salute = False
_tasksTodo = "test"

num = 3
integer = 1



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
def storepassword():
    print("TODO")

def rotor(text, shift, alphabets):

    def shift_Alphabet(alphabet):

        return alphabet[shift:] + alphabet [:shift]

    shifted_Alphabets = tuple(map(shift_Alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_Alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet) 
    return text.translate(table)
    
# If i want to invert it, I will just subtract (26 - shift)
_tasksTodo = rotor(_tasksTodo, 7, [string.ascii_lowercase, string.ascii_uppercase])
print(_tasksTodo)

def func():
    outfile = open("app.txt", "a")

    outfile.write(_tasksTodo + "\n")

    outfile.close()

    if input("To see the To do list press (T)") == "T":
        outfile = open("app.txt", "r")


        content = outfile.read()

        print(rotor(content, 19 , [string.ascii_lowercase, string.ascii_uppercase]))

    else:
        sys.exit
            


if __name__ == "__main__" and _tasksTodo != "": 
    func()
