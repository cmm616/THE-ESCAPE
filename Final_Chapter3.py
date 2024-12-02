
import globalvars


Peaked = False

def C3Introduction():
    print("The light grows brighter as you climb the spiral staircase. The room is empty, but you hear a rustling upstairs, it sounds like footsteps pacing back and forth. You notice a torch on the wall and a desk with two drawers. A cool breeze slips through the hole in the cobblestone. You have now reached the illuminated cellar, you see a desk, a staircase leading to the 1st floor and a foggy mirror. You feel like you’re being watched…")
    input()
    C3Decision()
def C3Decision():

    print("1. Return to Dungeon.")
    print("2. Go Upstairs")
    print("3. Search Desk Drawer 1")
    print("4. Seearch Desk Drawer 2")
    print("5. Clear Fog On Mirror")
    print("6. Peak through door.")
    print("7. Break Mirror")
    
    try:
        choice = int(input())
        
    except:
        print("Use numbers 1-7, No Letters!")
        C3Decision()
        choice = -1            
    match choice:
        case 1:
            C3Choice1()  
        case 2:
            C3Choice2()
        case 3:
            C3Choice3()
        case 4:
            C3Choice4()
        case 5:
            C3Choice5()
        case 6:
            C3Choice6()
        case 7:
            C3Choice7()
        case _:
            print("Use numbers 1-6")
            C3Decision()
def C3Choice1():
    globalvars.curr_chap = 2
    input()
    return
def C3Choice2():
    print("You have slain the goblin and took his kicks, the mercenary cannot hear your steps, be careful.")
    if "Sneaky Shoes" in globalvars.Player_inventory:
        globalvars.curr_chap = 4
        return
    else:
        print("Your Were Caught. Game Over!")
        input()
        globalvars.Game_is_Running = False
        return
def C3Choice3():
    print("You Find a Wanted Poster, What does it say? Wanted for the murder and sacrifice of the monarchs 6th born. 666 gold piece reward")
    globalvars.Player_inventory.append("Wanted Poster")
    input()
    C3Decision()
def C3Choice4():
    if "Silver_Key" in globalvars.Player_inventory:
        print("Obtain Attic Key")
        globalvars.Player_inventory.append("Attic Key")
    else:
        print("Drawer is locked. Requires Silver Key.")
    input()
    C3Decision()
def C3Choice5():
    print("You see your reflection.")
    if "Wanted Poster" in globalvars.Player_inventory:
        print("So it's me in the wanted poster...")
    C3Decision()
def C3Choice6():
    print("You notice a sleeping mercenary, and a drunk goblin.")
    global Peaked
    Peaked = True
    C3Decision()
def C3Choice7():
    if Peaked == False:
        print("That isnt an option pick 1-6.")
        C3Decision()
    else:
        print("You have broken the mirror")
        if "Longsword" in globalvars.Player_inventory:
            print("You have slain the Goblin and obtained Sneaky Shoes.")
            globalvars.Player_inventory.append("Sneaky Shoes")
            C3Decision()
        else:
            print("You have been caught. Game Over!")
            input()
            globalvars.Game_is_Running = False
            return
