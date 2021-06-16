import os
import pyttsx3
import speech_recognition as sr
from playsound import playsound
playsound('aws_menu_ready.mp3')

while True:

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t   WELCOME TO AWS MENU")
    print("\t\t\t\t#####################")
    os.system("tput setaf 3")
    print("""
                                                                           * To create key pair
                                                                           * To create security group
                                                                           * To launch an instance
                                                                           * To create S3 bucket
                                                                           * To delete key pair
                                                                           * To delete S3 bucket
                                                                           * To start an instance
                                                                           * To stop an instance
                                                                           * To create an extra volume
                                                                           * To attach extra volume to the instance
                                                                           * To detach extra volume to the instance
                                                                           * To delete the instance
                                                                           * To exit from the AWS(Cloud) menu
    """)
    os.system("tput setaf 3")
    print("\t\t\t\t####################")
    os.system("tput setaf 5")

    recogniser = sr.Recognizer()
    
    playsound('iamlistening.mp3')
    
    print(" I am Listening")
    with sr.Microphone() as mic:
        recogniser.adjust_for_ambient_noise(mic , duration=0.2)    
        speech=recogniser.listen(mic , phrase_time_limit=4  ) 
        playsound('input_recorded.mp3')
        print("Input recorded...!")
        ch  =  recogniser.recognize_google(speech, language="en-IN")
        print(ch)
    
    if ((("create" in ch) or ("generate" in ch)) and (("key" in ch) or ("key pair" in ch))):
       key_name = input("Enter key name :")
       os.system("aws ec2 create-key-pair  --key-name {}".format(key_name))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("security group" in ch) or ("firewall" in ch))):
       
       desc = input("Enter the Firewall description :")
       group_name = input("Enter the name you want to allocate to the firewall :")
       
       print("Information about the available VPCs is given below")
       os.system("aws ec2 describe-vpcs")
       vpc_name = input("Enter the vpc name :")
       
       os.system("aws ec2 create-security-group --group-name {}  --description '{}' --vpc-id {}".format(group_name,desc,vpc_name))
#        Dummy security Group Created , now we need to add rules to this Security Group 
       
       print(""" Adding Rules to the Security Group that we created  , In order to do that we need three things 
                        1.Protocol(tcp/udp)
                        2.Port Number
                        3.CIDR """)
       protocol = input("Enter the Protocol : ")
       port = input("Enter the Port Number : ")
       cidr = input("Enter the CIDR : ")
       os.system('aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3}'.format(group_name, protocol, port, cidr))
       input("Press Enter to continue")       


    elif ((("run" in ch) or ("execute" in ch) or ("launch" in ch) ) and (("a instance" in ch) or ("os" in ch) or ("a virtual machine"))):
       print(""" Enter the image from which you want to launch the Instance/VM
                Here are some popular and most used AMI's that can be used:-
                          1. Amazon AMI ->  ami-010aff33ed5991201
                          2. Redhat(RHEL8 AMI) -> ami-06a0b4e3b7eb7a300""")
                          
       img_name = input("Enter your image id:")
       
       i_type = input("Enter instance type (for example t2.micro) :")
       
       print(" Key pairs Available in this region")
       os.system(" aws ec2 describe-key-pairs ")
       
       key_name = input("Enter your key pair name :")
       
       print(" Security Groups Available in this region")
       os.system("aws ec2 describe-security-groups")
       sg_group = input("Enter the Security group id :")
       os.system("aws ec2 describe-subnets")
       sub = input("Enter subnet-id :")
       
       os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {} --count 1 ".format(img_name,i_type,key_name,sg_group,sub))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("s3 bucket" in ch) or ("bucket" in ch) or ("object storage" in ch))):
       buc_name = input("Enter a Unique bucket name :")
       reg = input("Region for the bucket to be deployed(for example:- ap-south-1(Mumbai) :")
       
       os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={} ".format(buc_name,reg,reg))       
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("key" in ch) or ("key pair" in ch))):
       print("Select the keypair you want to delete , here's a list of keypairs available in this region")
       os.system(" aws ec2 describe-key-pairs ")
       key_name = input("Name of the key-pair which you want to delete :")
       os.system(" aws ec2 describe-key-pairs ")
       os.system("aws ec2 delete-key-pair --key-name {} ".format(key_name))
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("bucket" in ch) or ("s3 bucket" in ch))):
       buc_name = input("Unique bucket name which you want to delete :")
       os.system("aws s3api delete-bucket --bucket {}".format(buc_name))
       print()

    elif (("start" in ch) and (("instance" in ch) or ("OS" in ch))):
       print("List of the instances in this region")
       os.system ("aws ec2 describe-instances")
       ins_id = input("Enter instance id which you want to start :")
       os.system("aws ec2 start-instances --instance-ids {}".format(ins_id))
       print()

    elif (("stop" in ch) and (("instance" in ch) or ("OS" in ch))):
       ins_id = input("Enter instance id which you want to stop :")
       os.system("aws ec2 stop-instances --instance-ids {}".format(ins_id))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("volume" in ch) or ("EBS volume" in ch) or ("Extra volume"))):
       av_zone = input("Enter the availability zone where you want to create volume: for example <ap-south-1b>")
       
       size = input("Enter the size of volume ,example 1G :")
       
       v_type = input("Enter the volume type <standard>:")
       
       os.system("aws ec2 create-volume --availability-zone {} --size {} --volume-type {}".format(av_zone,size,v_type))
       print()

    elif ((("attach extra volume" in ch) or ("add extra volume" in ch)) and (("to the instance" in ch) or ("to the OS" in ch))):
       vol_name = input("Enter the device name of the volume which you want to attach ex. /dev/sdh :")
       
       os.system ("aws ec2 describe-instances")
       ins_id = input("Enter your instance id by refering to the above details of the instances :")
       
       os.system ("aws ec2 describe-volumes")
       vol_id = input("Enter volume id by refering to the above details of the volumes:")
       os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(vol_name,ins_id,vol_id))
       print()

    elif ((("detach" in ch) or ("remove" in ch)) and (("volume" in ch) or ("EBS volume" in ch) or ("Extra volume" in ch))):
       os.system ("aws ec2 describe-volumes")
       v_id = input("Enter the extra volume id :")
       
       os.system("aws ec2 detach-volume --volume-id {}".format(v_id))
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("the instance" in ch) or ("the OS" in ch))):
       os.system ("aws ec2 describe-instances")
       i_id = input("Enter the instance id which you want to terminate :")
       os.system("aws ec2 terminate-instances --instance-ids {}".format(i_id))
       print()

    elif ((("exit from" in ch) or ("return back" in ch)) and (("to main menu" in ch) or ("cloud menu" in ch) or ("a w s menu"))):
       os.system("exit")
       break

    else:
        print("Invalid option")
    input("Enter to run more aws menu...")
    os.system("clear")
