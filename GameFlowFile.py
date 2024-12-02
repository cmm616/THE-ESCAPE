
import Final_Chapter1
import Final_Chapter2
import Final_Chapter3
import Final_Chapter4
import Final_Chapter5
import globalvars

def Gameflow():
    globalvars.Init()
    while globalvars.Game_is_Running:
        match globalvars.curr_chap:
            case 1:
                Final_Chapter1.C1Introduction()
            case 2:
                Final_Chapter2.C2Introduction()
            case 3:
                Final_Chapter3.C3Introduction()
            case 4:
                Final_Chapter4.C4Introduction()
            case 5:
                Final_Chapter5.C5Introduction()
    
    Game_Over()        
   
def Game_Over():
    print("Game Over! ") 
    Gameflow()
    
Gameflow()   


