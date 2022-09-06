#This code isn't intended for serious usage, this just a random code.
def isValider(num):
    numStr = str(num)
    preval = 0   
    l = 0 
    for i in numStr:
        if i == " ":
            continue
        k = int(i)
        l = l + (k*2)
        print(l)
        
        
if __name__ == '__main__':
    isValider("3523 6552 1234 5469")
