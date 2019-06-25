#Experimento!  
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
