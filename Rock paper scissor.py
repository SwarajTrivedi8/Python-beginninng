import random
def getchoices():
    a=input("Enter the word- ")
    b=["Rock","paper","Scissor"]
    k=random.choice(b)
    m={"player":a,"computer":k}
    return m
def checkwin(player,computer):
    print("you choose-",player,"computer choose-",computer)
    if player==computer:
        return "It is a tie"
    elif player=="Scissor":
        if computer=="paper":
            print("player wins")
        else:
            print("Computer wins")
    elif player=="Rock":
        if computer=="Scissors":
            print("player wins")
        else:
            print("Computer wins")
    elif player=="paper":
        if computer=="Rock":
            print("player wins")
        else:
            print("Computer wins")
m=getchoices()
result=checkwin(m["player"],m["computer"])
print(result)