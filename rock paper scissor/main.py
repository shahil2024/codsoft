import random
choice = ["Rock", "Paper", "Scissor"]
while True:
    print("Rock Paper Scissor Game:")
    youwin,computerwin=0,0
    for i in range(1,6):
        print("Round",i,"Start:")
        print("please select ant one option:")
        print("1.Rock", "2.Paper", "3.Scissor",sep="\n")
        yourchoice=int(input())
        if yourchoice==1:
            print("you select Rock")
            yourchoice="Rock"
        elif yourchoice==2:
            print("you select Paper")
            yourchoice="Paper"
        elif yourchoice==3:
            print("you select Scissor")
            yourchoice="Scissor"
        else:
            print("Invalid choice")
            break
        computerchoice=random.choice(choice)
        print("computer select:", computerchoice)

        if yourchoice==computerchoice:
            youwin+=1
            computerwin+=1
            print("This Round is Draw:")
        elif(yourchoice=="Paper" and computerchoice=="Rock") or (yourchoice=="Rock" and computerchoice=="Scissor") or (yourchoice=="Scisssor" and computerchoice=="Paper"):
            youwin+=1
            print("you win this Round")
        else:
            computerwin+=1
            print("computer win this Round")

    if youwin>computerwin:
        print("you win the game:")
        print("score is:", "your score:", youwin, "computer score:", computerwin,sep=" ")
    elif computerwin>youwin:
        print("you lose the game. computer win the game:")
        print("score is:", "your score:", youwin, "computer score:", computerwin,sep=" ")
    else:
        print("Match Draw")
        print("score is:", "your score:", youwin, "computer score:", computerwin,sep=" ")
    user_choice=input("Want to play again?(yes/Exit)")
    if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES':
        continue
    else:
        break