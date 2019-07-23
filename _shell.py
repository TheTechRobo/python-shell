#made using Python 3.6.5
#TtR M
#Setup
me = 0
egg = 0
tie = 0
runThru = 0
Insult = 0
exitOffendant = 0
import time
import os #Now I can control the OS using commands
#New commands made when the script starts, to make the if txt == ... more compact  
def exitShell(): #make a new command called exitShell() that does the following: 
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
    purge
    swan
    Ajira Airways
    what plane should I fly
    cmd --amount
    what is your favourite character in Lost
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
    print("Welcome to CustPy 0.10.5! thanks for using!  ") #output all that
def activ():
    win = input("Is your OS the following: Windows? (y/n, case-sensitive)
    if win == "y":
        os.system(start activ.bat)
    else:
        activate = input("What command?")
        key = input("What key?")
        print("Okay, processing your data.....")
        print("SyntaxError: Key Invalid! ")
        key()
def key():
    print("Unable to connect to Blacksmith.")
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
            print("This is CustPy Shell 0.10.5. Thanks for using! ")
        elif txt == "ver":
            ver() #run the ver() command (lines 18 and 19)
        elif txt == "VER": #Python is case-sensitive so i'm making user's lives easier ;)
            ver()
        elif txt == "ls": #if they type ls
            ls() # run the newly-made ls() command (lines 9 through 16)
        elif txt == "LS":
            ls() # same thing
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
                print("SyntaxError: not gonna happen)
        elif txt == "update":
            up2down()
        elif txt == "purge":
            print("That's not nice to the DHARMA folk!")
        elif txt == "swan"
            numbersExec = input(">: ")
            if numbersExec == "4815162342":
                print("SyntaxError: you forgot EXECUTE")
            elif numbersExec == "4 8 15 16 23 42":
                print("SyntaxError: you forgot EXECUTE")
            elif numbersExec == "4 8 15 16 23 42 EXECUTE":
                print('''
            ________________________________
            |    1  | 0  | 8  | 0  | 0     |
            ________________________________
            ''')
            elif numbersExec == "4 8 15 16 23 42 execute":
                print('''
            ________________________________
            |    1  | 0  | 8  | 0  | 0     |
            ________________________________
            ''')
            elif numbersExec == "4815162342 execute":
                print('''
            ________________________________
            |    1  | 0  | 8  | 0  | 0     |
            ________________________________
            ''')
            elif numbersExec == "4815162342 EXECUTE":
                print('''
            ________________________________
            |    1  | 0  | 8  | 0  | 0     |
            ________________________________
            ''')
            else: 
                print("Hello?")
                response = input()
                print("Who is this?")
                response = input()
                print("Dad?")
                print("Achievement Unlocked: Walt")
            print("Achievement Unlocked: The Numbers")
            achieveNumber = 1
        elif txt == "Ajira Airways":
            print("Flight 316")
        elif txt == "what plane should I fly":
            print("Oceanic Flight 815")
        elif txt == "cmd --amount":
            print("You have typed a command " +runThru "times")
        elif txt == "what is your favourite character in Lost":
            print("Desmond all the way!") #While I was typing De, it came out Sw. He worked in the Swan...
            #The keys on a keyboard of Desm and Swan are RIGHT BESIDE each other! Wow.
        elif txt == "you suck":
            print("Don't type i hate you or you'll be sorry")
            Insult = 1
        elif txt == "i hate you":
            print("Leave an issue on GitHub if you don't like it")
            if Insult == 1:
                print(1007988720 / 3800 * 4887987304487 - 663.314159)
            else:
                print("We can talk about it")
        elif txt == "swan --usage":
            print('''
            ORIENTATION
            
            This is the orientation text for the Swan station. I am Marvin Candle, the founder of DHARMA. 
            
            Every time you type this command, you must enter the code. 
            If you attempt to use the Computer for anything other than the Code, there may be another—
            
            Thank you for being a member of the DHARMA Initiative. In 540 days, your replacements will arrive. 
            ''')
        else: #If the user types anything else
            print("Unknown Command. Type ls for everything")
        if exitOffendant == 1:
            exit()
        runThru = runThru + 1
        if Insult == 1:
            exitOffendant = 1
Shell()
