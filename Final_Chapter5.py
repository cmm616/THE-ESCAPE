
import globalvars




def C5Introduction():
    print("Once in the locked attic you notice a sacrificial altar with the face of the 6th monarch. “Have I been set up?” The feeling of being framed seems all to real. What is that smell….? You have entered the attic, the moonlight shines on a shrine. What is that smell….? You can see an open window and a wall filled with symbols, what do these mean? You feel like you’re being watched…")
    input()
    C5Decision()
def C5Decision():
    print("1. Climb Down Ladder.")
    print("2. Inspect Shrine.")
    print("3. Look Out The Window.")
    print("4. Inspect Symbols.")
    print("5. Ignite Shrine and Escape.")
    print("6. Investigate Smell...")
    try:
        choice = int(input())
        
    except:
        print("Use numbers 1-6, No Letters!")
        C5Decision()
        choice = -1           
    
    
    match choice:
        case 1:
            C5Choice1()
        case 2:
            C5Choice2()
        case 3:
            C5Choice3()
        case 4:
            C5Choice4()
        case 5:
            C5Choice5()
        case 6:
            C5Choice6()
        case _:
            print("Use numbers 1-6")
            C5Decision()



    

def C5Choice1():
     globalvars.curr_chap = 4
     return
def C5Choice2():
    print("The shire is blood-soaked, though there seems to be a picture of the recently passed 6th monarch.")
    input()
    C5Decision()
def C5Choice3():
    print("I need to understand what’s going on before I leave.”) - (The breezy air is refreshing)")
    input()
    C5Decision()
def C5Choice4():
    print("You see several pentagrams...")
    input()
    C5Decision()
def C5Choice5():
    if "Unlit Torch" in globalvars.Player_inventory:
        print("The fire spreads to the rest of the building, you have been framed for the sacrifice of the 6th monarch.”)")
        input()
        globalvars.Game_is_Running = False
        return
    else:
        print("You have nothing to light this shrine on fire. find a torch.")
    C5Decision()
def C5Choice6():
    print("You notice a small burlap sack, containing the small body of the 6th monarch, it reeks…")
    input()
    C5Decision()