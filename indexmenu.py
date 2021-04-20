import os
import getpass
import speech_recognition as sr

password = getpass.getpass("Password : ")
if password != "gaurav":
    print("Wrong Password")
    exit()
else:
    while True:
         print("\n")
         os.system("tput setaf 1")
         print("\t\t\t\t  WELCOME TO MAIN MENU")
         print("\t\t\t\t\t\####################")
         os.system("tput setaf 2")
         print("""
                                                                                 1. To execute or launch Linux Operation
                                                                                 2. To execute or launch Docker Opearation
                                                                                 3. To execute or launch AWS(Cloud) Opearation
                                                                                 4. To execute or launch Hadoop Operation
                                                                                 5. To exit or stop 
         """)
         os.system("tput setaf 6")
         print("\t\t\t\t\#####################")
         os.system("tput setaf 7")

         r = sr.Recognizer()
         with sr.Microphone() as source:
             print("Please speak anything")
             audio = r.listen(source)
             print("Your voice is recording please wait")

         ch = r.recognize_google(audio)
         print(ch)
         if ((("linux" in ch) or ("Linux" in ch) or ("linux operation" in ch)) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 linux_command.py")

         elif ((("docker" in ch) or ("Docker" in ch) or ("docker operation" in ch)) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 docker.py")

         elif ((("aws" in ch) or ("AWS" in ch) or ("cloud operation" in ch)) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 aws-operation.py")

         elif ((("hadoop" in ch) or ("Hadoop" in ch) or ("hadoop operation" in ch)) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 hadoop.py")

         elif ((("exit" in ch) or ("return" in ch)) and (("from main menu" in ch) or ("menu" in ch))):
             os.system("exit")
             break

         else:
             print("Wrong Option try again")

         input("Enter to run more main menu...")
         os.system("clear")


