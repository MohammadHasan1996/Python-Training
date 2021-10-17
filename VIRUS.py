from subprocess import check_output
import platform
import time


print ("Please run this code on Virtual Machine")
time.sleep(5)
x = str(input("Please enter the extension you are looking for (NO DOTS):"))
def find_drives():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
    sys_drive = []
    cmd = check_output("wmic logicaldisk get name", shell = True)
    for i in drive:
        if i in str(cmd):
            sys_drive.append(i)

    return sys_drive
drive = find_drives()

print(drive)



def find_files():
    for i in drive:
        cmd = check_output(str(i)+"&& dir /S *."+x,shell = True)
    return cmd

find_files()


def Create_File():
    for i in drive:
        FILE = check_output(str(i) + "&& dir /S *." + x + ">>%userprofile%\\desktop\\Your_Files.txt", shell=True)

Create_File()
print("Next step is erasing your files")
time.sleep(3)
Final_Warning = str(input("Are you sure you want to continue????(y/n)"))
if Final_Warning =="y":
    def Delete_File():
        for i in drive:
            DEL = check_output(str(i) + "&& del /S *." + x, shell=True)


    Delete_File()
    print("Your files are fucked up!!!")

elif Final_Warning =="n":
    pass















