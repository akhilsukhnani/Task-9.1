import os
import speech_recognition as sr

while True:  

    print("\n")
    os.system("tput setaf 3")
    print("\t\t\t\tWELCOME TO LINUX MENU")
    print("\t\t\t\t####################################")
    os.system("tput setaf 5")
    print("""
                                                                                            1. To view or show date
                                                                                            2. To view show calendar
                                                                                            3. To execute or run calculator
                                                                                            4. Create User
                                                                                            5. Create Directory
                                                                                            6. View the RAM Usage
                                                                                            7. View the CPU Information
                                                                                            8. Check the IP address
                                                                                            9. Create file
                                                                                           10. To scan ip using nmap
                                                                                           11. To go out from linux menu
    """)
    os.system("tput setaf 1")
    print("\t\t\t\t####################################")
    os.system("tput setaf 2")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak anything")
        audio = r.listen(source)
        print("Your voice is recording please wait")

    ch = r.recognize_google(audio)
    print(ch)
    if ((("run" in ch) or ("execute" in ch) or ("view" in ch)) and (("date" in ch) or ("date command" in ch))):
        os.system("date")
        print()

    elif ((("run" in ch) or ("execute" in ch) or ("view" in ch)) and (("calendar command" in ch) or ("calendar" in ch))):
        os.system("cal")
        print()

    elif ((("run" in ch) or ("execute" in ch) or ("view" in ch)) and (("bc" in ch) or ("binary calculator" in ch))):
        os.system("bc")
        print()

    elif ((("create" in ch) or ("add" in ch)) and (("user" in ch) or ("new user" in ch))):
        print("Enter user name :",end ='')
        u_name = input()
        os.system("useradd {}".format(create_user))
        print()

    elif ((("create" in ch) or ("make" in ch)) and (("folder" in ch) or ("directory" in ch))):
        print("Enter directory name :",end ='')
        d_name = input()
        os.system("mkdir {}".format(d_name))
        print()

    elif ((("view" in ch) or ("total free" in ch)) or ("watch" in ch) and (("ram" in ch) or ("RAM" in ch))):
        os.system("free -m")

    elif ((("view" in ch) or ("total" in ch) or ("run" in ch)) and (("CPU utilization" in ch) or ("CPU information" in ch) or ("CPU" in ch))):
        os.system("lscpu")

    elif ((("watch" in ch) or ("view" in ch) or ("check" in ch)) and (("IP address" in ch) or ("IP" in ch))):
        os.system("ifconfig")

    elif ((("make" in ch) or ("create" in ch)) and ("file" in ch)):
        print("Enter file name :",end = '')
        f_name = input("Enter the file name")
        location = input("Enter the location :")
        os.system("touch {}/{}".format(location,f_name))
        print()
  
    elif ((("run" in ch) or ("execute" in ch) or ("check" in ch)) and (("connectivity" in ch) or ("ping" in ch))):
        print("Enter IP :",end = '')
        ip = input()
        os.system("ping {}".format(ip))
        print()

    elif ((("exit from" in ch) or ("return back" in ch)) and (("main menu" in ch) or ("linux menu"))):
        os.system("exit")
        break
       
    else:
        print("Invalid Choice")
    input("Enter to run more linux menu...")
    os.system("clear")

