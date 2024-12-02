
import globalvars


def C4Introduction():
    print("You have reached the first floor. You can finally see the outside through a distant window, it’s the middle of the night. The sleeping mercenary has yet to awake, “should I try to sneak past him, or should I slay him and be done with it…?” You notice a ladder leading to the attic. The mercenary has a ring of keys around his wrist. You have just escaped the cellar, with sneaky shoes, your footsteps can’t be heard. The exit door appears right behind the sleeping guard…")
    input()
    C4Decision()
def C4Decision():
    print("1. ATTACK SLEEPING GUARD.")
    print("2. CLIMB LADDER TO ATTIC.")
    print("3. RETURN TO CELLAR.")
    
    try:
        choice = int(input())
        
    except:
        print("Use numbers 1-3, No Letters!")
        C4Decision()
        choice = -1           
    
    
    match choice:
        case 1:
            C4Choice1()
        case 2:
            C4Choice2()
        case 3:
            C4Choice3()
        case _:
            print("Use numbers 1-3")
            C4Decision()

def C4Choice1():
    print("You Are Outmatched! Game over")
    input()
    globalvars.Game_is_Running = False
    return
def C4Choice2():
    if "Attic Key" in globalvars.Player_inventory:
        globalvars.curr_chap = 5
    else:
        print("ATTIC DOOR LOCKED, REQUIRES AN -ATTIC KEY-.")
        input()
        C4Decision()
def C4Choice3():
    globalvars.curr_chap = 3
    return