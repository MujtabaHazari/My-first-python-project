'''
Rock = 1
Paper = -1
Scissors = 0
'''
import random #random is a method
computer = random.choice([1,-1,0])  

youstr = input("Enter your choice: ")
youdict = {"r":1,"p":-1,"s":0}
you = youdict[youstr]

reversedict = {1:"Rock", -1:"Paper", 0:"Scissors"}
print(f"You have choosen {reversedict[you]} \nComputer has choosen {reversedict[computer]} ")

if(computer==you):
    print("Its a draw \n'Try again'")

else:
    if(computer==1 and you==-1):  #nested if else
        print("You Won!")
    elif(computer==-1 and you==0):
        print("You Won!") 
    elif(computer==0 and you==1):
        print("You Won!") 
    elif(computer==-1 and you==1):
        print("You Lose!") 
    elif(computer==0 and you==-1):
        print("You Lose!") 
    elif(computer==1 and you==0):
        print("You Lose!") 
    else:
        print("something went wrong!")
    
    

