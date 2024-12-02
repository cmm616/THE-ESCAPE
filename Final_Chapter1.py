#Corinthian M
#11/7/2024
#Chapter 1
import globalvars

choice = 4


def C1Introduction():
    print("You wake up in a cell on a damp cot, you notice a bucket and a crack in the wall. It’s dark. “Who am I? Where am I? How can I escape?” These questions linger as you feel a strange presence watching you…")
    input()
    C1Decision()



def C1Decision():
    print("1. Go back to sleep.")
    print("2. Look through the crack in the cells wall.")
    print("3. Try to open the cell door.")
    print("4. Check bucket.")
    choice = int(input())
    try:
        match choice:
            case 1:
                option1()
            case 2:
                option2()
            case 3:
                option3()
            case 4:
                option4()
            case _:
                print("Use numbers 1-4.")
                C1Decision()
    except:
        print("Use numbers 1-4, No Letters!")
        C1Decision()

def option1():
    print("i'm not tired.")
    input()
    C1Decision()

def option2():
    print("It's to dark to see anything.")
    input()
    C1Decision()

def option3():
    if "Rustedcellkey" in globalvars.Player_inventory:
        globalvars.curr_chap = 2
        return
    else:
        print("The Door is Locked, Requires Rusted Cell Key To Open.")
        C1Decision()    



def option4():
    print("You find a key called: Rusted cell key")
    globalvars.Player_inventory.append("Rustedcellkey")
    input()
    C1Decision()



