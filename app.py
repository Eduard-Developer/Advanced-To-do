from code import interact
import time
import sys
import string
Todolist = ["."]



salute = False
_tasksTodo = ""

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



def func():
    outfile = open("app.txt", "w")

    outfile.write(_tasksTodo + "\n")

    outfile.close()

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

testtext = "hello this will be encrypted"
print(rotor(testtext, 7, [string.ascii_lowercase, string.ascii_uppercase]))

#time.sleep(0.5)
#if input("Do you want to set up a Password (Y/N)") == "Y":
    #print("await: yes")
           # else:
           # print("await: no")
    
func()

