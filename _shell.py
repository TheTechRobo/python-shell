#made using Python 3.6.5
#TtR M
#New commands made when the script starts, to make the if txt == ... more compact  
def exitShell(): #make a new command called exitShell() that does the following: 
    input("You're SURE you want to exit CustPy? ") #ask if they're sure
    input("Like really sure? ")
    yn = input("Then type y. (If you're unsure type n) ")
    if yn == "y": #if they type y
        print('Stopping services.......')
        print("21%.........")
        time.sleep(1)
        print("96%......")
        time.sleep(0.2)
        print("97%.....")
        time.sleep(0.12)
        print("99%......")
        time.sleep(0.21)
        print('100%..')
        print("Stopping chatterbox daemon, done")
        print('Exiting...')
        exit() #exit program
    else: #otherwise
        Shell() #go back to the Shell()
def ls():
        print('''COMMAND LIST
NOTE: you MUST type these commands EXACTLY as written. Like if it says cls you can't type Cls

    win
    sudo rm -Rf / --no-preserve-root
    sing this song to You
    I need help
    help
    HELP
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
    swan --usage
    swan --usage --splice
    sudo flip-coin process coinResult
    sudo cpy-get install flip-coin
    ''')
def up2down():
	if lac == "y":
		print("Trying three ways")
		os.system('git https://github.com/TheTechRobo/python-shell/archive/omega!!.zip')
		works = input("Did that work? (without syntax error?")
		if works == "y":
			os.system('curl -O https://github.com/thetechrobo/python-shell/archive/omega!!.zip')
		else:
			os.system('wget https://github.com/thetechrobo/python-shell/archive/omega!!.zip')
			works = input("Did that work?")
			if works == "y":
				os.system('echo Now you will have to decompress a ZIP')
			else:
				from tqdm import tqdm
				import requests
				url = "https://raw.githubusercontent.com/TheTechRobo/python-shell/omega!!/_shell.py"
				response = requests.get(url, stream=True)
				with open("_shell", "wb") as handle:
					for data in tqdm(response.iter_content()):
						handle.write(data)
def ver(): #make a new command called ver()
    print("Welcome to CustPy 0.14! thanks for using!") #output all that
def activ():
	if win == "y":
		os.system('start activ.bat')
	elif linmac == "y":
		os.system('chmod +x activ.sh')
		os.system('activ.sh')
	else:
		activate = input("What command?")
		key = input("What key?")
		print("Okay, processing your data.....")
		print("SyntaxError: Key Invalid! ")
		keyStore()
def keyStore():
    print("Unable to connect to Blacksmith.")
def startUp():
    #Setup
    me = 0
    egg = 0
    tie = 0
    runThru = 0
    import time #now I can use time
    import os #now I can control the OS using commands
    import random #now I can use randomness
    #Stuff
    win = input("Is your OS Windows? (y/n, case-sensitive)")
    if win == "n":
        lac = input("Linux or Mac? (y/n, case-sensitive)")
        if lac == "n":
            print("Then we'll have to revert to the old-fashioned way")
    jokes = ["Infusing with Caffiene.......", "Loading Nothing........", "Why can't you be coding this instead of using this?", "Loading Peeves......"]
    jokeOfChoice = random.choice(jokes)
    print(jokeOfChoice)
    time.sleep(2)
    print("Loaded all the good stuff (but not the bad)")
def amountOfCmds():
	print("You have typed a command " +runThru +"times")
print()
startUp()
print()
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
            print("This is CustPy Shell 0.14. Thanks for using!")
        elif txt == "ver":
            ver() #run the ver() command (lines 18 and 19)
        elif txt == "VER": #Python is case-sensitive so I'm making user's lives easier ;)
            ver()
        elif txt == "ls": #if they type ls
            ls() #run the ls() command (lines 9 through 16)
        elif txt == "LS":
            ls() #same thing
        elif txt == "exit":
            print("Starting exit daemon....")
            exitShell()
        elif txt == "EXIT":
            exitShell()
        elif txt == "help":
            print("HELP MODE. Type ls for commands. Know that parts of it are case-sensitive. I tried to cover it up the best I could but it led to bugs sometimes. ")
        elif txt == "slate":
            print("slate has been delayed, sorry for the inconvenience")
        elif txt == "I need help":
            print("HELP MODE. Type ls for commands. Know that parts of it are case-sensitive. I tried to cover it up the best I could but it led to bugs sometimes. ")
        elif txt == "":
            print("Please type a command")
        elif txt == "laugh":
            print("Open a new Python session, then type from __future__ import braces and look at the error. ") #A python joke
            print("Redirecting to the Interweb. Fasten your seatbelts and make sure the Internet is connected")
            time.sleep(2)
            import antigravity #A comic strip
        elif txt == "I need a laugh":
            print("Open a new Python session, then type from __future__ import braces and look at the error. ") #A python joke
            print("Redirecting to the Interweb. Fasten your seatbelts and make sure the Internet is connected")
            import antigravity
        elif txt == "clear":
            if win == "y":
                os.system('cls')
            elif lac == "y":
                os.system('clear')
            else:
                for i in range(0, 21):
                    print()
        elif txt == "cls":
            if win == "y":
                os.system('cls')
            elif lac == "y":
                os.system('clear')
            else:
                for i in range(0, 21):
                	print()
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
            if me != 1:
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
            if tie != 1: 
            	print("SyntaxError: not gonna happen")
        elif txt == "update":
            up2down()
        elif txt == "purge":
            print("That's not nice to the DHARMA folk!")
        elif txt == "swan":
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
            elif numbersExec == "4 8 15 16 23 32":
                print('"It\'s 42," said Jack')
            elif numbersExec == "4815162332":
                print('"It\'s 42," said Jack')
            elif numbersExec == "4 8 15 16 23 32 EXECUTE":
                print("SyntaxError: you gotta be kidding me. We've got Locke??")
            elif numbersExec == "4 8 15 16 23 32 execute":
                print("SyntaxError: you gotta be kidding me. We've got Locke??")
            elif numbersExec == "4815162332 execute":
                print("SyntaxError: you've got to be kidding me. We've got Locke??")
            elif numbersExec == "4815162332 EXECUTE":
                print("SyntaxError: Good grief. We've got Locke??")
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
            amountOfCmds()
        elif txt == "what is your favourite character in Lost":
            print("Desmond all the way!") #While I was typing De, it came out Sw. He worked in the Swan...
            #The keys on a keyboard of Desm and Swan are RIGHT BESIDE each other! Wow.
        elif txt == "swan --usage":
            print('''
            ORIENTATION
            
            This is the orientation text for the Swan station. I am Marvin Candle, the founder of DHARMA. 
            
            Every time you type this command, you must enter the code, to prevent--
            Never attempt to use the Computer for anything other than the Code, because there may—
            
            Thank you for being a member of the DHARMA Initiative. In 540 days, your replacements will arrive. 
            ''')
        elif txt == "swan --usage --splice":
            print('''
            ORIENTATION
            
            This is the orientation text for the Swan station. I am Marvin Candle, the founder of DHARMA. 
            
            Every time you type this command, you must enter the Code to prevent another Incident—and prevent a global collapse. 
            You should not attempt to use the Computer for anything other than the Code, because there may be another Incident. 
            
            Thank you for being a member of the DHARMA Initiative. In 540 days, your replacements will arrive. 
            ''')
        elif txt == "sudo flip-coin process coinResult":
            if coinPkg == "installed":
                flips = int(input('how many times do you want to flip the coin? '))
                outcomes = ['head','tail']
                wieghts = [.5,.5]
                head=0
                tail=0
                for flip in range(flips):
                    h_t = random.choice(outcomes)
                    if h_t == 'head':
                        head += 1
                    else:
                        tail += 1
                    def percentage(ht,outcome):
                        global flips
                        percent = outcome/flips * 100
                        print('{}: {}%'.format(ht,"%.2f" % percent))
                    percentage('head',head)
                    percentage('tail',tail)
            elif coinPkg == "notInstalled":
                print("coinFlip is not installed, use 'sudo cpy-get install cFlip' to install")
            elif coinPkg == "noSameKey":
                print('''Alert! coinFlip does not have a valid key anymore
                This probably means that the developer forgot to update the key, but it could mean it was tampered with
                Please try downloading again, with 'sudo cpy-verify install cFlip' instead''')
        elif txt == "sudo cpy-get install flip-coin":
            chances = [0, 1]
            keyProbab = random.choice(chances)
            if keyProbab == 0:
                print('''Searching cache........
                flip-coin is a symb-link to cFlip. Please take caution, this may be someone tricking you into downloading a virus
                Installing in sandbox mode
                Verifying...........
                The identity of the developer has been confirmed as TheTechRobo''')
                Yn = input("this will take 0kB on your system. Continue (Y/n, case-sensitive)")
                if Yn == "Y":
                    print("Downloading archives, done")
                    print("Installing app, done")
                    print("Updating symb-links.......")
                    time.sleep(1)
                    print("Done. Updating files.....")
                    time.sleep(3.14159265358979)
                    print("Done. Please wait.......")
                    time.sleep(0.5)
                    print("Finished with errors")
                    coinPkg = "noSameKey"
            else:
                print('''Searching cache........
                flip-coin is a symb-link to cFlip. Please take caution, this may be someone tricking you into downloading a virus
                Installing in sandbox mode
                Verifying...........
                The identity of the developer has been confirmed as TheTechRobo''')
                Yn = input("this will take 0kB on your system. Continue (Y/n, case-sensitive)")
                if Yn == "Y":
                    print("Downloading archives, done")
                    print("Installing app, done")
                    print("Updating symb-links.......")
                    time.sleep(1)
                    print("Done. Updating files.....")
                    time.sleep(3.14159265358979)
                    print("Done. Please wait.......")
                    time.sleep(0.5)
                    print("Finished successfully!")
                    coinPkg = "installed"
    if txt == "sudo cpy-verify install flip-coin":
        print('''Searching cache........
		flip-coin is a symb-link to cFlip. Please take caution, this may be someone tricking you into downloading a virus
                Installing with verification
                Verifying...........
                The identity of the developer has been confirmed as TheTechRobo''')
        Yn = input("this will take 0kB on your system. Continue (Y/n, case-sensitive)")
        if Yn == "Y":
            print("Downloading archives, done")
            print("Installing app, done")
            print("Updating symb-links.......")
            time.sleep(1)
            print("Done. Updating files.....")
            time.sleep(3.14159265358979)
            print("Done. Please wait.......")
            time.sleep(0.5)
            print("Scanning, done")
            print("Finished successfully!")
            coinPkg = "installed"
    elif txt == "sawyerism":
        for i in range(0, 19):
            print()
            print("Loading list......")
            sawyerisms = ["Hey Freckles", "Morning yourself", "the guy who looks like he's from a Burt Reynolds movie"]
            print("Picking random Sawyerism....")
            sawyerismOfChoice = random.choice(sawyerisms)
            print(sawyerismOfChoice)
    else: #If the user types anything else
        print("Unknown Command. Type ls for everything")
    runThru = runThru + 1
Shell()
