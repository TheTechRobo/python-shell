#made using Python 3.6.5
#it's omega!!!!!!!!!!!!
#TtR M
#Setup
me = 0
egg = 0
tie = 0
import time
#New commands, to make the if txt == blah more compact  
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
        print('Exiting...')
        exit() #exit program
    else: #otherwise
        Shell() # go back to the Shell()
def ls():
        print('''COMMAND LIST
NOTE: you MUST type these commands EXACTLY as written. Like if it says cls you can't type Cls

    win
    sudo rm -Rf / --no-preserve-root
    sing this song to You
    I need help
    help
    ls
    ver
    VER
    4 8 15 16 23 42
    4 8 15 16 23 42 EXECUTE
    laugh
    I need a laugh
    cls
    clear
    look at me
    I found the egg
    what'd you stop for, Doc?
    no you're not
    activateCmd
    ''')
def up2down():
    from tqdm import tqdm
    import requests
    url = "https://raw.githubusercontent.com/TheTechRobo/python-shell/omega!!/_shell.py"
    response = requests.get(url, stream=True)
    with open("_shell", "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
def ver(): #make a new command called ver()
    print("Welcome to CustPy 0.9.11! thanks for using!  ") # output all that
def activ():
    activate = input("What command?")
    key = input("What key?")
    print("Okay, processing your data.....")
    print("SyntaxError: Key Invalid! ")
#Main loop
def Shell(): #define command Shell()
    while True: # do all this section in a loop (when done, restart)
        txt = input("Last Login: Unknown. !") #Add the prompt
        if txt == "win": #If user types win
            print("This ain't MS-DOS") #output "This ain't MS-DOS"
        elif txt == "sudo rm -Rf / --no-preserve-root": #IF user types sudo rm -Rf /
            print("Deleted Everything, Including Nothing") # etc etc etc
        elif txt == "sing this song to You":
            print("It goes like this: the fourth the fifth...")
        elif txt == "version":
            print("This is CustPy Shell 0.9.11. Thanks for using! ")
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
            print("slate has been delayed, sorry for the inconvenience")
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
            print("Redirecting to the Interweb. Fasten your seatbelts and make sure the Internet is connected")
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
        elif txt == "egg":
            if egg == 1:
                print("What more do you want from me? I have nothing left to offer you.")
            else: 
                print("YOU FOUND AN EASTER EGG!!")
            egg = 1
        elif txt == "look at me":
            print("I'm the king of New York!")
            me = 1
        elif txt == "no you're not":
            if me == 1:
                print("Oh yeah, you're the king of New York. My bad. I must have the words wrong")
            else:
                print("I'm not what again?")
        elif txt == "activateCmd":
            activ()
        elif txt == "I found the egg":
            if egg == 1:
                print("Yes, you did! Congrats!")
            else: 
                print("Liar, liar, pants on fire, stuck in a dryer on a telephone wire!")
        elif txt == "what'd you stop for, Doc?":
            print("Gotta tie up my shoe!")
            print("Command activated:well Dopey here just stepped on my foot")
            tie = 1
        elif txt == "well Dopey here just stepped on my foot!":
            if tie == 1:
                print("Gee, Grumpy, maybe your foot was in the wrong spot.")
                print("I'll show you spots, you big galoot!")
             else: 
                print("SyntaxError: CommandNotActive)
        elif txt == "update":
            up2down()
        else: #If the user types anything else
            print("Unknown Command. Type ls for everything")
Shell()
