import os
import speech_recognition as sr

while True:

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t  WELCOME TO DOCKER MENU")
    print("\t\t\t\t#######################")
    os.system("tput setaf 4")
    print("""
                                                                                           1. For installing docker
                                                                                           2. For checking docker is installed
                                                                                           3. To start docker service
                                                                                           4. To see the downloaded docker images
                                                                                           5. For download any docker image
                                                                                           6. To launch container
                                                                                           7. To see total running docker container
                                                                                           8. To stop the container
                                                                                           9. To delete any docker image
                                                                                          10. To configure web server in container
                                                                                          11. To exit from docker menu
    """)
    os.system("tput setaf 1")
    print("\t\t\t\t###################")
    os.system("tput setaf 4")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak anything")
        audio = r.listen(source)
        print("Your voice is recording please wait")

    ch = r.recognize_google(audio)
    print(ch)
    if ((("install" in ch) or ("download" in ch)) and (("docker" in ch) or ("docker software" in ch))):
        os.system("sudo yum install docker-ce --nobest -y")
        print()

    elif ((("check" in ch) or ("look" in ch) or ("Look" in ch))  and (("docker-ce" in ch) or ("docker software" in ch))):
        os.system("sudo rpm -qa | grep docker")
        print()

    elif ((("start" in ch) or ("enable" in ch) or ("make permanent" in ch)) and (("docker" in ch) or ("docker services" in ch))):
        os.system("sudo systemctl start docker")
        os.system("sudo systemctl enable docker")
        print()
            
    elif ((("look" in ch) or ("check" in ch) or ("Look" in ch)) and (("image" in ch) or ("images" in ch) or ("docker images" in ch))):
        os.system("sudo docker images")
        print()

    elif ((("download" in ch) or ("downloading" in ch)) and (("image" in ch) or ("images" in ch) or ("docker images" in ch))):
        print("Enter image name :")
        img_name = input()
        os.system("sudo docker pull {}".format(img_name))
        print()

    elif ((("run" in ch) or ("launch" in ch) or ("execute" in ch)) and (("os" in ch) or ("container" in ch) or ("docker container" in ch))):
        os_name = input("Enter container name :")
        img_name = input("Enter image name :")
        os.system("sudo docker run -dit --name {} {}".format(os_name,img_name))
        print()

    elif ((("look" in ch) or ("check" in ch) or ("Look" in ch)) and (("total running OS" in ch) or ("total running container" in ch) or ("total running docker container" in ch))):
        os.system("sudo docker ps")

    elif (("stop" in ch) and (("os" in ch) or ("container" in ch) or ("docker container" in ch))):
         os_name = input("Enter container name :")
         os.system("sudo docker stop {}".format(os_name))
         print()

    elif ((("remove" in ch) or ("delete" in ch)) and (("image" in ch) or ("images" in ch) or ("docker images" in ch))):
         img_name = input("Enter image name :")
         os.system("sudo docker rmi {}".format(img_name))
         print()
               
    elif ((("Run" in ch) or ("configure" in ch)) and ("web server" in ch)):
         os.system("sudo yum install httpd")
         os.system("sudo systemctl start httpd")
         print()

    elif ((("exit from" in ch) or ("return back" in ch)) and (("docker menu" in ch) or ("main menu" in ch))):
         os.system("exit")
         break
    
    else:
         print("Invalid choice")
    input("Enter to run more docker menu...")
    os.system("clear")


