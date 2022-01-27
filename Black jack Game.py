#!/usr/bin/env python -i
Acc_input = float(input("The cash you want to play with?"))
Acc_amont = Acc_input

while True:
    print("---------------------------------")
    StartQ = input("Do you wanna play? Y/N ")
    if StartQ == "N":
        break
    else:
        print("---------------------------------")
        print("Your account : %0.2f dh" %(Acc_amont))
        Bet = float(input("Put your bet here: "))
        Acc_amont -= Bet
        print("Your account : %0.2f dh" %(Acc_amont))
        WinOrLoss = input("Did you won or lost or push? W/L/P ")
        if WinOrLoss == "W": Acc_amont = Acc_amont + (Bet * 2)
        elif WinOrLoss == "P": Acc_amont += Bet
        elif WinOrLoss =="L": Acc_amont += 0 
        print("Your account : %0.2f dh" %(Acc_amont))
    