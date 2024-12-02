import globalvars


def C2Introduction():
    print("“Strange there are only four cells in this corridor and a spiral staircase with a dim light illuminating the furthest stair. Should I check the other cells before I venture upstairs? That feeling of being watched has gone away now, what was that?”")
    input()
    C2Decision()

def C2Decision():
    print(" 1. Return to cell- ") 
    print(" 2. Search cell 2 ") 
    print(" 3. search cell 3 ") 
    print(" 4. Search cell 4 ") 
    print(" 5. Go Upstairs. ")
    
    try:
        choice = int(input())
        
    except:
        print("Use numbers 1-5, No Letters!")
        C2Decision()
        choice = -1            

    match choice:
        case 1:
            C2Choice1()
        case 2:
            C2Choice2()
        case 3:
            C2Choice3()
        case 4:
            C2Choice4()
        case 5:
            C2Choice5()
        case _:
            print("Use numbers 1-5")
            C2Decision()

def C2Choice1():
    globalvars.curr_chap = 1
    return
def C2Choice2():
    print("You find an Unlit Torch.")
    globalvars.Player_inventory.append("Unlit Torch")
    input()
    C2Decision()

def C2Choice3():
    if "Silver_Key" in globalvars.Player_inventory:
        print("Obtain Longsword.")
        globalvars.Player_inventory.append("Longsword")
    else:
        print("Door is locked. Requires Silver Key.")
    input()
    C2Decision()
def C2Choice4():
    print("You found a Silver Key")
    globalvars.Player_inventory.append("Silver_Key")
    input()
    C2Decision()
def C2Choice5():
    globalvars.curr_chap = 3
    return