#made using Python 3.6.5
#Almost omega!!!!!!!!!!!!
#TtR M
import time
def exitShell(): #if the user wants to exit
    yn = input("Sure you want to exit CustPyth? (y/n)") #ask if they're sure
    if yn == "y": #if they type y
        print('Stopping Services.......')
        print("25%.........")
        time.sleep(1)
        print("96%......")
        time.sleep(0.2)
        print("97%.....")
        time.sleep(0.2)
        print("98%.....")
        time.sleep(0.12)
        print("99%......")
        time.sleep(0.46)
        print('100%..')
        exit() #exit program
    else: #otherwise
        pass # do nothing
def ls():
    print('''    win
    sudo rm -Rf / --no-preserve-root
    sing this song to You
    ver
    I need help
    help
    ls
    4 8 15 16 23 42
    4 8 15 16 23 42 EXECUTE
    laugh
    I need a laugh
    cls
    clear
    ''')
def ver(): #make a new command called ver()
    print("Welcome to CustPy 0.8! thanks for using! Almost omega!!!! ") # output all that
def Shell(): #define command Shell()
    while True: # do all this section in a loop (when done, restart)
        txt = input("Last Login: Unknown. !") #Add the prompt
        if txt == "win": #If user types win
            print("This ain't MS-DOS") #output "This ain't MS-DOS"
        elif txt == "sudo rm -Rf / --no-preserve-root": #IF user types sudo rm -Rf /
            print("Deleted Everything, Including Nothing") # etc etc etc
        elif txt == "sing this song to You":
            print("It goes like this: The Fourth The Fifth...")
        elif txt == "version":
            print("This is CustPy Shell 0.8. Thanks for using! Close to omega! We are right now at gamma-the-hut :)")
        elif txt == "ver":
            ver() #run the ver() command (18 and 19)
        elif txt == "VER": #Python is case-sensitive so i'm making user's lives easier ;)
            ver()
        elif txt == "ls": #if they type ls
            ls() # run the newly-made ls() command (lines 9 through 16)
        elif txt == "exit":
            print("Starting exit daemon....")
            exitShell()
        elif txt == "help":
            print("HELP MODE. Type ls for commands. Know that parts of it are case-sensitive. I tried to cover it up the best I could but it led to bugs sometimes. ")
        elif txt == "slate":
            print("slate has been delayed")
            print("Sorry for the inconvenience")
            #Not there yet
        elif txt == "I need help":
            print("HELP MODE. Type ls for commands. Know that parts of it are case-sensitive. I tried to cover it up the best I could but it led to bugs sometimes. ")
        elif txt == "4 8 15 16 23 42":
            print("You didn't press EXECUTE")
        elif txt == "4 8 15 16 23 42 EXECUTE":
            print('''
            ________________________________
            |    1  | 0  | 8  | 0  | 0     |
            ________________________________
            ''')
        elif txt == "laugh":
            print("Open a new Python session, then type from __future__ import braces and look at the error. ") #A python joke
            import antigravity #A comic strip
        elif txt == "I need a laugh":
            print("Open a new Python session, then type from __future__ import braces and look at the error. ") #A python joke
            print("Redirecting to the Interweb. Fasten your seatbelts and make sure the Internet is connected")
            import antigravity
        elif txt == "clear":
            print('''




























            ''')
        elif txt == "cls":
            print('''




























            ''')       
        else: #If the user types anything else
            print("Unknown Command. Type ls for everything")
Shell()
