from code import interact
import time
import sys
import string
Todolist = ["."]



salute = False
_tasksTodo = "blabla"
actual_tasksTodo = "blabla"

num = 3
integer = 1


donotuse_alpthabet = string.ascii_lowercase

print("the alphabet is working and it is: ", str(donotuse_alpthabet))
if str(donotuse_alpthabet[1]) == "a":
    print("the first letter is a so it should be fine")

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
    _tasksTodo = actual_tasksTodo
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

actual_tasksTodo = rotor(_tasksTodo, 7, [string.ascii_lowercase, string.ascii_uppercase])
print(rotor(_tasksTodo, 7, [string.ascii_lowercase, string.ascii_uppercase]))

def func():
    outfile = open("app.txt", "a")

    outfile.write(actual_tasksTodo + "\n")

    outfile.close()

if __name__ == "__main__" and actual_tasksTodo != "": 
    func()

