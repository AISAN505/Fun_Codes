import os

Acc_input = float(input("How you want to play with? "))
print("---------------------------------")
Acc_amont = Acc_input
# dh is my country currency, you can change to yours e.g $ £ € etc.
while True:
    StartQ = input("Another round (Y/N)? ")
    # Here the game starts
    if StartQ == "N" or StartQ == "n": break
    else:
        print("---------------------------------")
        print("Your account : %0.2f dh" %(Acc_amont))
        Bet = float(input("Input your bet: "))
        Acc_amont -= Bet
        print("Your current balance : %0.2f dh" %(Acc_amont))
        # If you win, you win :)
        WinOrLoss = input("Won(W), Lost(L), Push(P)? ")
        if WinOrLoss == "W" or WinOrLoss == "w": Acc_amont = Acc_amont + (Bet * 2)
        elif WinOrLoss == "P" or WinOrLoss == "p": Acc_amont += Bet
        elif WinOrLoss =="L" or WinOrLoss == "l": Acc_amont += 0 
        print("Your current balance : %0.2f dh" %(Acc_amont))
    os.system('clear')
