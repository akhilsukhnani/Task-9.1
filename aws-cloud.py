import os
import speech_recognition as sr

while True:

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t   WELCOME TO AWS MENU")
    print("\t\t\t\t#####################")
    os.system("tput setaf 3")
    print("""
                                                                           1. To create key pair
                                                                           2. To create security group
                                                                           3. To launch an instance
                                                                           4. To create S3 bucket
                                                                           5. To delete key pair
                                                                           6. To delete S3 bucket
                                                                           7. To start an instance
                                                                           8. To stop an instance
                                                                           9. To create an extra volume
                                                                           10. To attach extra volume to the instance
                                                                           11. To detach extra volume to the instance
                                                                           12. To delete the instance
                                                                           13. To exit from the AWS(Cloud) menu
    """)
    os.system("tput setaf 3")
    print("\t\t\t\t####################")
    os.system("tput setaf 5")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak anything")
        audio = r.listen(source)
        print("Your voice is recording please wait")
    
    ch = r.recognize_google(audio)
    print(ch)
    if ((("create" in ch) or ("generate" in ch)) and (("key" in ch) or ("key pair" in ch))):
       key_name = input("Enter key name :")
       os.system("aws ec2 create-key-pair  --key-name {}".format(key_name))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("security group" in ch) or ("firewall" in ch))):
       desc = input("Enter the description :")
       group_name = input("Enter a group name :")
       vpc_name = input("Enter a vpc name :")
       os.system("aws ec2 create-security-group --group-name {}  --description '{}' --vpc-id {}".format(group_name,desc,vpc_name))
       print()

    elif ((("run" in ch) or ("execute" in ch) or ("launch" in ch)) and (("instance" in ch) or ("os" in ch))):
       img_name = input("Enter your image:")
       i_type = input("Enter instance type :")
       key_name = input("Enter your key pair :")
       sg_group = input("Enter Security group id :")
       sub = input("Enter subnet-id :")
       os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {} --count 1 ".format(img_name,i_type,key_name,sg_group,sub))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("s3 bucket" in ch) or ("bucket" in ch))):
       buc_name = input("Unique bucket name :")
       reg = input("Region for the bucket to be deployed :")
       os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={} ".format(buc_name,reg,reg))       
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("key" in ch) or ("key pair" in ch))):
       key_name = input("Name of the key-pair which you want to delete :")
       os.system("aws ec2 delete-key-pair --key-name {} ".format(key_name))
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("bucket" in ch) or ("s3 bucket" in ch))):
       buc_name = input("Unique bucket name which you want to delete :")
       os.system("aws s3api delete-bucket --bucket {}".format(buc_name))
       print()

    elif (("start" in ch) and (("instance" in ch) or ("OS" in ch))):
       ins_id = input("Enter instance id which you want to start :")
       os.system("aws ec2 start-instances --instance-ids {}".format(ins_id))
       print()

    elif (("stop" in ch) and (("instance" in ch) or ("OS" in ch))):
       ins_id = input("Enter instance id which you want to stop :")
       os.system("aws ec2 stop-instances --instance-ids {}".format(ins_id))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("volume" in ch) or ("EBS volume" in ch) or ("Extra volume"))):
       av_zone = input("Enter the availability zone where you want to create volume :")
       size = input("Enter the size of volume :")
       v_type = input("Enter the volume type :")
       os.system("aws ec2 create-volume --availability-zone {} --size {} --volume-type {}".format(av_zone,size,v_type))
       print()

    elif ((("attach extra volume" in ch) or ("add extra volume" in ch)) and (("to the instance" in ch) or ("to the OS" in ch))):
       vol_name = input("Enter the device name of the volume which you want to attach ex. /dev/sdh :")
       ins_id = input("Enter your instance id :")
       vol_id = input("Enter volume id :")
       os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(vol_name,ins_id,vol_id))
       print()

    elif ((("detach" in ch) or ("remove" in ch)) and (("volume" in ch) or ("EBS volume" in ch) or ("Extra volume" in ch))):
       v_id = input("Enter the extra volume id :")
       os.system("aws ec2 detach-volume --volume-id {}".format(v_id))
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("the instance" in ch) or ("the OS" in ch))):
       i_id = input("Enter the instance id which you want to terminate :")
       os.system("aws ec2 terminate-instances --instance-ids {}".format(i_id))
       print()

    elif ((("exit from" in ch) or ("return back" in ch)) and (("main menu" in ch) or ("Cloud menu" in ch))):
       os.system("exit")
       break

    else:
        print("Invalid option")
    input("Enter to run more aws menu...")
    os.system("clear")
