#made using Python 3.6.5
#TtR M
import time
def exitShell(): #if the user wants to exit
    yn = input("Sure you want to exit CustPyth? (y/n)") #ask if they're sure
    if yn == "y": #if they type y
        print('Stopping Services.......')
        print("25%.........")
        time.sleep(1)
        print("96%......")
        print('100%..')
        exit() #exit program
    else: #otherwise
        pass # do nothing
def ls():
    print('''    win
    sudo rm -Rf / --no-preserve-root
    Sing this Song to YOU
    ver
    I need help
    help
    ls **CURRENT COMMAND**
    ''')
def version(): #make a new command called help()
    print("Welcome to CustPy 0.4.3.1! thanks for using!  ") # output all that
def Shell(): #define command Shell()
    while True: # do all this section in a loop (when done, restart)
        txt = input("Last Login: Unknown. !") #Add the prompt
        if txt == "win": #If user types win
            print("This ain't MS-DOS") #output this ain't MS-DOS
        elif txt == "sudo rm -Rf / --no-preserve-root": #IF user types sudo rm -Rf /
            print("Deleted Everything, Including Nothing") # etc etc etc
        elif txt == "Sing this Song to YOU":
            print("It goes like this: The Fourth The Fifth...")
        elif txt == "version":
            print("This is CustPy Shell 0.4.3.2. Thanks for using!")
        elif txt == "ls": #if they type ls
            ls() # run the newly-made ls() command (lines 9 through 16)
        elif txt == "ver":
            version() #run the version() command (18 and 19)
        elif txt == "exit":
            print("Starting exit daemon....")
            exitShell()
        elif txt == "help" or "I need help":
            print("HELP MODE. Type ls for commands. Know that parts of it are case-sensitive. I tried to cover it up the best I could but it led to bugs sometimes. ") 
        elif txt == "slate":
            print("Slate:Alpha")
            #Snake Experiments
            #SLATE text editor
            #Version 0.1.1
            print("Going to save files in directory _shell.py is in. If you want to exit, type exit,!")
            while True:
                mode = input("Mode: a for append, w for overwrite. Case-sensitive. ")
                if mode == "a":
                    file = input("Filename?")
                    if file == "exit,!":
                        print("Not developed yet")
                        #Shell()
                    else:
                        my_file = open(file, "a") #open user file as append
                        my_file.write(input("Type a line. ")) #Append to the file

                else:
                    file = input("Enter filename: ")
                    if file == "exit,!":
                        print("If you did this in the actual version it would restart the shell.")
                        #Shell()
                    else:
                            my_file = open(file, "w")  #open user-chosen file as readwrite
                            my_file.write(input("Type a line. ")) #Write to the file
            
        else: #If the user types anything else
            print("Unknown Command. Type ls for everything")
Shell()
