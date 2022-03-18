# os to read, subprocess to use cmd without opening a seperate console window
import subprocess
import os

# win10toast is optional
try:
    from win10toast import ToastNotifier
except:
    subprocess.call("python -m pip instsall win10toast", shell=True)
    from win10toast import ToastNotifier

mode = input("Upload [U] \nAnalysis [A] \nFilter [F] \nDebug [D] \n>>> ")


if mode == "U":
    report = open('report.txt', 'w')

    for path, subdirs, files in os.walk(os.getcwd()):
        for name in files:
            if not(os.path.getsize(os.path.join(path, name)) >= 681574400):
                if os.path.join(path, name)[len(os.getcwd())+1:] in ('report.txt', 'report2.txt', 'report3.txt'):
                    continue
                print("Scanning: " + os.path.join(path, name)[len(os.getcwd())+1:])
                report.write(os.popen("vt analysis " + os.popen("vt scan file "+str(os.path.join(path, name)[len(os.getcwd())+1:])).read().split(' ')[1]).read())

    report.close()

if mode == "A":
    status = open('report.txt', 'r')
    newthing = open('report2.txt', 'w')
    for i in status:
        if "_id:" in i:
            print("Writing analysis for "+i[8:-2]+" to report2.txt")
            newthing.write(os.popen('vt analysis '+i[8:-2]).read())
    newthing.close()

if mode == "F":
    newthing = open('report2.txt', 'r')
    listem = newthing.readlines()
    for i in listem:
        if "result: " in i:
            if not("null" in i):
                print(i)
        if "status: " in i:
            print(i)
    newthing.close()

if mode == "D":
    bruh = os.popen('vt analysis YTgwOGM1YTI1NWQyMmRmMzY2ZDYzNzcxMGYxMDY5YzY6MTY0NjIwMDI3Mw==').read()
    print(repr(bruh))
    print(bruh)

toaster = ToastNotifier()
toaster.show_toast("Finished scanning", "Check output")
            
